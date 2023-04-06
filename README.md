# IoT-Mqtt-Based-garment-production-dashboard
A dashboard to display the process of garment manufacturing on a Dynamic dashboard with the help of an IoT RF reader at each stage

Dependencies being used - 
1. Paho Mqtt - Python library for mqqt client (pip install)
2. sqlite3 - to handle database (pip install)
3. Flask - To build dashboard
4. Mosquitto mqtt broker (need to install separately)



Run the createdb.py to create a sample database if not already created.

Run flask-dashboard to start local flask server.


Make sure mosquitto is up and running -
  use "mosquitto_pub -t my/topic -m rfidcode_status" in cmd to simulate a garment tap.
  for sample data 
    rfidcode values range [1,3]
    status values range [1,3]
