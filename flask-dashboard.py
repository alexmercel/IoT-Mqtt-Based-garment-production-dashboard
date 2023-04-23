from flask import Flask, render_template, request, redirect, url_for,jsonify
import paho.mqtt.client as mqtt
from datetime import datetime
import sqlite3
import matplotlib.pyplot as plt
import createdb
createdb.createnew()
app = Flask(__name__)

# Define MQTT broker settings
broker_address = "localhost"
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
    global percentage_comp_dict
    global logs
    global errors
    print("Received message: " + msg.payload.decode())
# Retrieve the article ID from the message payload
    mq_payload = msg.payload.decode().split("_")   
    article_id = str(mq_payload[0])
    article_status=int(mq_payload[1])
    print ("Article ID extracted is "+ article_id)

# Connect to the SQLite database
    conn = sqlite3.connect('mydatabasenew.db')
    c = conn.cursor()

# Retrieve the article information from the database based on the ID
    c.execute('SELECT * FROM inventory WHERE rfid=?', (article_id,))
    row = c.fetchone()
# Close the database connection
    conn.close()
    print ("Details fetched from inventory ", row)
# If the article was found, append it to the logs list
    if row is not None:
        conn = sqlite3.connect('mydatabasenew.db')
        c = conn.cursor()
        ts= datetime.now().isoformat()
        try:
            c.execute('INSERT INTO worklogs (rfid,stage_status,operator,time_stamp) VALUES (?,?,"Mohan",?)',(article_id,article_status,ts,))
            print("insert sucessfull")
        except:
            errors="Invalid Stage: Article already passed stage "+str(article_status)
            print (errors)
        conn.commit()
        c.close()
        conn.close()
        logs=getWorklogs()
        items_comp=calc_items_in_stage(logs,linecap)
        percentage_comp=[items/linecap*100 for items in items_comp]
        #create percentage_comp as dict with keys one,two,three
        percentage_comp_dict=dict(zip(['one','two','three'],percentage_comp))
        print("completed:",items_comp)
        print(percentage_comp_dict)
        print(logs)
    else:
        errors="Invalid Article: Article not present in database"

# Set MQTT client callbacks
client.on_connect = on_connect
client.on_message = on_message

# A dictionary of valid user credentials for the example
VALID_CREDENTIALS = {
    'admin': 'password123'
}

# Initialize messages list
logs = []

#Initialize error list
errors = []
#Function to get worklog entries from database
def getWorklogs():
    conn = sqlite3.connect('mydatabasenew.db')
    c = conn.cursor()
    c.execute('INSERT INTO worklogs (rfid,stage_status,operator,time_stamp) VALUES ("fcf053d3",1,"Mohan",?)',(datetime.now().isoformat(),))

    c.execute('SELECT w.time_stamp, w.rfid, i.name, i.description, w.stage_status, w.operator, i.line FROM inventory i, worklogs w WHERE w.rfid = i.rfid ORDER BY w.time_stamp DESC')
    logs=[]
    for i in (c.fetchall()):
        log = {
            'time_stamp': i[0],
            'article_id': i[1],
            'article_name': i[2],
            'article_description': i[3],
            'stage_status': i[4],
            'operator': i[5],
            'line': i[6]
            }
        logs.append(log)
    return (logs)

#Calculate number of items in each stage
def calc_items_in_stage(messages,linecap):
    items_stage_wise=[0,0,0]
    for i in messages:
        if i['stage_status']==1:
            items_stage_wise[0]+=1
        elif i['stage_status']==2:
            items_stage_wise[1]+=1
        elif i['stage_status']==3:
            items_stage_wise[2]+=1
    
    return (items_stage_wise)


    
#Initialize lines variables in a dict as [A:x1,B:x2] where A, B are lines and x1,x2 are efficiencies
linecap=10
percentage_comp=[]
items_comp=[]
percentage_comp_dict={'one':0,'two':0,'three':0}

# Connect to MQTT broker
client.connect(broker_address, broker_port)

#Define User
user="Admin"
# Start MQTT client loop in a separate thread
client.loop_start()

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# A dictionary of valid user credentials for the example
VALID_CREDENTIALS = {
    'admin': 'password123',
    'patil': 'patil'
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    global user
    
    username = request.form.get('username')
    password = request.form.get('password')
    user=username

    # Check if the entered credentials match the valid credentials
    if username in VALID_CREDENTIALS and VALID_CREDENTIALS[username] == password:
        # If the credentials are valid, redirect to the admin dashboard
        return redirect(url_for('dashboard'))
    else:
        # If the credentials are invalid, display an error message
        error = 'Invalid username or password'
        return render_template('index.html', error=error)

# Define Flask route to display messages
@app.route('/dashboard')
def dashboard():
    # Get the most recent messages from the MQTT client
    global logs
    global errors
    error = errors
    errors= []
    progress = percentage_comp_dict
    print ('progress:',progress)

    return render_template("dashboard.html", messages=logs, errors=error ,num_messages=len(logs),items_comp=items_comp,progress=progress,user=user)

@app.route("/Prodline1")
def getProdline1():
    return jsonify(logs)
@app.route("/Prodline2")
def getProdline2():
    return jsonify(logs)
@app.route("/Prodline3")
def getProdline3():
    return jsonify(logs)
@app.route("/Prodline4")
def getProdline4():
    return jsonify(logs)
#Send data for each line page progress
@app.route("/dataProdline1")
def progressLine1():
    return jsonify([50,20,40])
@app.route("/dataProdline2")
def progressLine2():
    return jsonify([50,20,40])
@app.route("/dataProdline3")
def progressLine3():
    return jsonify([50,20,40])
@app.route("/dataProdline4")
def progressLine4():
    return jsonify([50,20,40])

@app.route('/filterline', methods=['GET'])
def filterline():
    datetime_strstart = request.args.get('datetimestart')
    datetime_strend = request.args.get('datetimeend')
    line=request.args.get('line')
    print(datetime_strend,datetime_strstart)
    datetime_objstart = datetime.strptime(datetime_strstart, '%Y-%m-%dT%H:%M')
    datetime_objend = datetime.strptime(datetime_strend, '%Y-%m-%dT%H:%M')
    logs=getWorklogs()
    result=[]
    bardata={}
    print (logs)
    for i in logs:
        if i['line']==line:
            if datetime_objstart <= datetime.strptime(i['time_stamp'],'%Y-%m-%dT%H:%M:%S.%f') <= datetime_objend:
                result.append(i)
    for i in result:
            try:
                bardata[i['operator']]+=1
            except:
                bardata[i['operator']]=1
    print (bardata)
    return jsonify(bardata)

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000,debug=True, threaded=True)
    # app.run()
