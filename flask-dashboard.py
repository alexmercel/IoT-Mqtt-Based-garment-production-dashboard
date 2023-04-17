from flask import Flask, render_template
import paho.mqtt.client as mqtt
from datetime import datetime
import sqlite3
import matplotlib.pyplot as plt

app = Flask(__name__)

# Define MQTT broker settings
broker_address = "192.168.43.203"
broker_port = 1883
topic = "my/topic"

# Initialize MQTT client
client = mqtt.Client()
client.username_pw_set("user", "pass")

# Define callback function for MQTT connect event
def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT broker")
    client.subscribe(topic)

# Define callback function for MQTT message event
def on_message(client, userdata, msg):
    print("Received message: " + msg.payload.decode())
        # Retrieve the article ID from the message payload
    mq_payload = msg.payload.decode().split("_")   
    article_id = str(mq_payload[0])
    article_status=int(mq_payload[1])
    print (article_id)

    # Connect to the SQLite database
    conn = sqlite3.connect('mydatabase.db')
    c = conn.cursor()

    # Retrieve the article information from the database based on the ID
    c.execute('SELECT * FROM articles WHERE id=?', (article_id,))
    row = c.fetchone()
    # Close the database connection
    conn.close()
    print (row)
    # If the article was found, append it to the messages list
    if row is not None:
        conn = sqlite3.connect('mydatabase.db')
        c = conn.cursor()
        timestamp= datetime.now().isoformat()
        
        c.execute('UPDATE articles SET status=?,time=? WHERE id=?', (article_status,timestamp, article_id))

        conn.close()
        message = {
            'timestamp': timestamp,
            'article_id': article_id,
            'article_name': row[1],
            'article_description': row[3],
            'status': article_status,
        }
        messages1.append(message)
        items_comp=calc_items_in_stage(messages1,linecap)
        percentage_comp=[items/linecap*100 for items in items_comp]
        #create percentage_comp as dict with keys one,two,three
        percentage_comp_dict1=dict(zip(['one','two','three'],percentage_comp))
        percentage_comp_dict.append(percentage_comp_dict1)
        print("completed:",items_comp)
        print(percentage_comp_dict)
        print(messages1)

# Set MQTT client callbacks
client.on_connect = on_connect
client.on_message = on_message

# Initialize messages list
messages1 = []
#Calculate number of items in each stage
def calc_items_in_stage(messages,linecap):
    items_stage_wise=[0,0,0]
    for i in messages:
        if i['status']==1:
            items_stage_wise[0]+=1
        elif i['status']==2:
            items_stage_wise[1]+=1
        elif i['status']==3:
            items_stage_wise[2]+=1
    
    return (items_stage_wise)


    
#Initialize lines variables in a dict as [A:x1,B:x2] where A, B are lines and x1,x2 are efficiencies
linecap=10
percentage_comp=[]
items_comp=[]
percentage_comp_dict=[{'one':0,'two':0,'three':0}]

# Connect to MQTT broker
client.connect(broker_address, broker_port)

# Start MQTT client loop in a separate thread
client.loop_start()

# Define Flask route to display messages
@app.route("/")
def messages():
    # Get the most recent messages from the MQTT client
    messages = messages1
    progress = percentage_comp_dict[-1]
    print ('progress:',progress)
    # Format the messages as a list of dictionaries with "timestamp" and "payload" keys datetime.fromtimestamp(message.timestamp)
    formatted_messages = [{"timestamp": message['timestamp'], "articleId": message['article_id'],"articleName": message['article_name'],"articleDesc": message['article_description'],"status": message['status']} for message in messages]
    # Pass the formatted messages to the template
    return render_template("messages.html", messages=formatted_messages, num_messages=len(messages1),items_comp=items_comp,progress=progress)

if __name__ == "__main__":
    app.run()
