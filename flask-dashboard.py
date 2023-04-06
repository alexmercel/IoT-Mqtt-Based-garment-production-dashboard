from flask import Flask, render_template
import paho.mqtt.client as mqtt
from datetime import datetime
import sqlite3

app = Flask(__name__)

# Define MQTT broker settings
broker_address = "localhost"
broker_port = 1883
topic = "my/topic"

# Initialize MQTT client
client = mqtt.Client()

# Define callback function for MQTT connect event
def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT broker")
    client.subscribe(topic)

# Define callback function for MQTT message event
def on_message(client, userdata, msg):
    print("Received message: " + msg.payload.decode())
        # Retrieve the article ID from the message payload
    mq_payload = msg.payload.decode().split("_")   
    article_id = int(mq_payload[0])
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
        c.execute('UPDATE articles SET status=? WHERE id=?', (article_status, article_id))

        conn.close()
        message = {
            'timestamp': datetime.now().isoformat(),
            'article_id': article_id,
            'article_name': row[1],
            'article_description': row[2],
            'status': article_status,
        }
        messages1.append(message)
        print(messages1)

# Set MQTT client callbacks
client.on_connect = on_connect
client.on_message = on_message

# Initialize messages list
messages1 = []

# Connect to MQTT broker
client.connect(broker_address, broker_port)

# Start MQTT client loop in a separate thread
client.loop_start()

# Define Flask route to display messages
@app.route("/")
def messages():
    # Get the most recent messages from the MQTT client
    messages = messages1
    # Format the messages as a list of dictionaries with "timestamp" and "payload" keys datetime.fromtimestamp(message.timestamp)
    formatted_messages = [{"timestamp": message['timestamp'], "articleId": message['article_id'],"articleName": message['article_name'],"articleDesc": message['article_description'],"status": message['status']} for message in messages]
    # Pass the formatted messages to the template
    return render_template("messages.html", messages=formatted_messages, num_messages=len(messages1))

if __name__ == "__main__":
    app.run()
