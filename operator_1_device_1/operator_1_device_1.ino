#include <SPI.h>
#include <MFRC522.h>
#include <Adafruit_MQTT.h>
#include <Adafruit_MQTT_Client.h>
#include <ESP8266WiFi.h>

// Wifi credentials
const char* ssid = "Abhishek's iPhone";
const char* password = "patilpatil2";

// MQTT credentials
const char* mqtt_server = "192.168.43.203";
const char* mqtt_username = "user";
const char* mqtt_password = "pass";
const int mqtt_port = 1883;
WiFiClient client;
Adafruit_MQTT_Client mqtt(&client, mqtt_server, mqtt_port, mqtt_username, mqtt_password);

// MQTT topic
const char* topic = "my/topic";

// RFID setup
MFRC522 mfrc522(4, 5);
String rfid;

void setup() {
  // Initialize serial communication
  Serial.begin(9600);

  // Connect to Wi-Fi
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }

  // Initialize RFID reader
  SPI.begin();
  mfrc522.PCD_Init();

  // Connect to MQTT broker
  while (!mqtt.connected()) {
  Serial.println("Connecting to MQTT broker...");
  if (mqtt.connect()) {
    Serial.println("MQTT connected");
  } else {
    Serial.print("MQTT connection failed, state=");
    Serial.println(mqtt.connected());
    delay(5000);
  }
}

}

void loop() {
  // Look for new RFID cards
  if (mfrc522.PICC_IsNewCardPresent() && mfrc522.PICC_ReadCardSerial()) {
    // Read the RFID card's UID
    rfid = "";
    for (byte i = 0; i < mfrc522.uid.size; i++) {
      rfid += String(mfrc522.uid.uidByte[i], HEX);
    }

    // Publish the RFID UID to the MQTT broker
    Adafruit_MQTT_Publish mqtt_pub = Adafruit_MQTT_Publish(&mqtt, topic);
    mqtt_pub.publish((rfid + "_1").c_str());
    Serial.println("RFID read: " + rfid);
  }

  // Keep the MQTT client connected
 if (!mqtt.ping()) {
  Serial.println("MQTT disconnected, reconnecting...");
  if (mqtt.connect()) {
    Serial.println("MQTT reconnected");
  } else {
    Serial.print("MQTT connection failed");
    delay(5000);
  }
}

  delay(1000);
}
