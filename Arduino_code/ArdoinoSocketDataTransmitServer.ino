// #include <ESP8266WiFi.h>

const char* ssid     = "Xiaomi_3D3E";
const char* password = "2019newpassword";
WiFiServer wifiServer(8080);
  
void setup() 
{
    pinMode(LED_BUILTIN,OUTPUT) ;

    Serial.begin(9600);

    WiFi.begin(ssid, password);
    while (WiFi.status() != WL_CONNECTED)
     { 
        digitalWrite(LED_BUILTIN, HIGH);   // turn the LED on (HIGH is the voltage level)
        delay(200);                        // wait for a second
        digitalWrite(LED_BUILTIN, LOW);    // turn the LED off by making the voltage LOW
        delay(200);                        // wait for a second
     }
    wifiServer.begin();
}

void loop()
{/*
  WiFiClient client = wifiServer.available();
  if (client) {
    while (client.connected()) {
      while (client.available()>0) {
        char c = client.read();
        if (c == '$'){
           lcd.clear();
           lcd.setCursor(0,0);
        }
        else;
        {
          //Serial.println(c);
          lcd.print(c);
        }
    }}
    client.stop();
    Serial.println("Client disconnected");
    lcd.clear();
    lcd.print("Client                                  disconnected");
   }
   */
 }