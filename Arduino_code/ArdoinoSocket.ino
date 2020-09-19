#include <ESP8266WiFi.h>
#include <ESP8266mDNS.h>
#include <WiFiUdp.h>
#include <ArduinoOTA.h>

#ifndef STASSID
#define STASSID "Xiaomi_3D3E";
#define STAPSK  "2019newpassword";
#endif

const char* ssid = STASSID;
const char* password = STAPSK;
WiFiServer wifiServer(8080);
int LED_BUILTIN = 2;

void setup() {
  pinMode(LED_BUILTIN,OUTPUT);
  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);
   while (WiFi.status() != WL_CONNECTED)
     { 
        digitalWrite(LED_BUILTIN, LOW);
        delay(200);
        digitalWrite(LED_BUILTIN, HIGH);
        delay(200);
     }
  while (WiFi.waitForConnectResult() != WL_CONNECTED) {
    delay(5000);
    ESP.restart();
  }

  // Port defaults to 8266
  // ArduinoOTA.setPort(8266);

  // Hostname defaults to esp8266-[ChipID]
  // ArduinoOTA.setHostname("myesp8266");

  // No authentication by default
  // ArduinoOTA.setPassword("admin");

  // Password can be set with it's md5 value as well
  // MD5(admin) = 21232f297a57a5a743894a0e4a801fc3
  // ArduinoOTA.setPasswordHash("21232f297a57a5a743894a0e4a801fc3");
  
  //ArduinoOTA.setPassword((const char *)"004424");
  ArduinoOTA.onStart([]() {
    String type;
    if (ArduinoOTA.getCommand() == U_FLASH) {
      type = "sketch";
    } else { // U_FS
      type = "filesystem";
    }

    // NOTE: if updating FS this would be the place to unmount FS using FS.end()
  });
  ArduinoOTA.onEnd([]() {
  });
  ArduinoOTA.onProgress([](unsigned int progress, unsigned int total) {
  });
  ArduinoOTA.begin();

//***************************************##***************************************//



if (true) //Old void setup() 
{
    digitalWrite(LED_BUILTIN, HIGH);
    wifiServer.begin();
    delay(2000);
    digitalWrite(LED_BUILTIN, LOW);
    
    delay(2000);

    digitalWrite(LED_BUILTIN, HIGH);
    Serial.begin(9600);
    delay(2000);
    digitalWrite(LED_BUILTIN, LOW);
    Serial.flush();

    int i = 0;
    while (i < 20)
    {
      if (Serial.available() > 0)
        {
          digitalWrite(LED_BUILTIN, HIGH);
          delay(50);
          i = i + 1;
          digitalWrite(LED_BUILTIN, LOW);
          Serial.flush();
          delay(50);
        }
      else
        {
          while (0 < 1)
          {
            digitalWrite(LED_BUILTIN, HIGH);
            delay(1000);
            digitalWrite(LED_BUILTIN, LOW);
            delay(500);
          }
        }
    }
}
}
  

void loop() {
  ArduinoOTA.handle();
//***************************************##***************************************//
  WiFiClient client = wifiServer.available();
  if (client) 
  {
    while (client.connected())
    {
      digitalWrite(LED_BUILTIN, HIGH); // Show that the client is conncted.
      int i = 0;
      while (i < 5)                    //Flash five times when conncted.
      {
        digitalWrite(LED_BUILTIN, HIGH);
        delay(50);
        i = i + 1;
        digitalWrite(LED_BUILTIN, LOW);
        delay(50);
      }
      if (Serial.available() > 0)
      {
        int data = client.read();
        client.print(data);
      }
    }
    client.stop();
    digitalWrite(LED_BUILTIN, LOW);
  }
}