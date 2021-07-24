#include "HX711.h"
#include "ESP8266WiFi.h"
#include "ESP8266WebServer.h"

/* Put your SSID & Password */
const char* ssid = "NodeMCU";  // Enter SSID here
const char* password = "12345678";  //Enter Password here

/* Put IP Address details */
IPAddress local_ip(192,168,1,1);
IPAddress gateway(192,168,1,1);
IPAddress subnet(255,255,255,0);

ESP8266WebServer server(80);

//SD Card
#include <SPI.h>
#include <SD.h>
File myFiletemp;
File myFileload;

//Load Cell
const int LOADCELL_DOUT_PIN = 12;
const int LOADCELL_SCK_PIN = 14;
float weight;
#define calibration_factor 419640
HX711 scale;

// Ignition System
int LEDG=16;
int IGN=4;
int BUZ=0;
int statusid = 0;
int val = LOW;

//Thermocouple
const int thermocouple_input = A0;
float adc_val;
float temperature;
bool emergencystatus;
bool systemstatus;

String SendHTML(uint8_t systemstatus,uint8_t emergencystatus, float temperature, float weight){
  String ptr = "<!DOCTYPE html> <html>\n";
  ptr +="<head><meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0, user-scalable=no\">\n";
  ptr +="<title>Static Rocket Test System</title>\n";
  ptr +="<style>html { font-family: Helvetica; display: inline-block; margin: 0px auto; text-align: center;}\n";
  ptr +="body{margin-top: 50px;} h1 {color: #444444;margin: 50px auto 30px;} h3 {color: #444444;margin-bottom: 50px;}\n";
  ptr +=".button {display: block;width: 80px;background-color: #1abc9c;border: none;color: white;padding: 13px 30px;text-decoration: none;font-size: 25px;margin: 0px auto 35px;cursor: pointer;border-radius: 4px;}\n";
  ptr +=".button-on {background-color: #1abc9c;}\n";
  ptr +=".button-on:active {background-color: #16a085;}\n";
  ptr +=".button-off {background-color: #34495e;}\n";
  ptr +=".button-off:active {background-color: #2c3e50;}\n";
  ptr +="p {font-size: 14px;color: #888;margin-bottom: 10px;}\n";
  ptr +="</style>\n";
  ptr +="</head>\n";
  ptr +="<body>\n";
  ptr +="<h1>ESP8266 Web Server</h1>\n";
  ptr +="<h3>Using Access Point(AP) Mode</h3>\n";
  
   if(systemstatus)
  {ptr +="<p>System Status: ON</p><a class=\"button button-off\" href=\"/systemoff\">OFF</a>\n";}
  else
  {ptr +="<p>System Status: ON</p><a class=\"button button-on\" href=\"/systemon\">ON</a>\n";}
  if(emergencystatus)
  {ptr +="<p>emergency Status: ON</p><a class=\"button button-off\" href=\"/emergencyoff\">OFF</a>\n";}
  else
  {ptr +="<p>emergency Status: OFF</p><a class=\"button button-on\" href=\"/emergencyon\">ON</a>\n";}
ptr += "<h1>Sensor to Node MCU Web Server</h1><h3>Data:</h3> <h4>"+String(temperature)+ ","+String(weight)+"</h4>";
ptr +="</body>\n";
ptr +="</html>\n";
return ptr;
}


void handle_OnConnect() 
{
  systemstatus = LOW;
  emergencystatus = HIGH;
  Serial.println("GPIO7 Status: OFF | GPIO6 Status: OFF");
  server.send(200, "text/html", SendHTML(systemstatus,emergencystatus, temperature, weight)); 
}

void handle_systemon() {
  systemstatus = HIGH;
  Serial.println("GPIO7 Status: ON");
  server.send(200, "text/html", SendHTML(true,emergencystatus, temperature, weight)); 
}

void handle_systemoff() {
  systemstatus = LOW;
  Serial.println("GPIO7 Status: OFF");;  server.send(200, "text/html", SendHTML(false,emergencystatus, temperature, weight)); 
}

void handle_emergencyon() {
  emergencystatus = HIGH;
  Serial.println("GPIO2 Status: ON");
  server.send(200, "text/html", SendHTML(systemstatus,true, temperature, weight)); 
}

void handle_emergencyoff() {
  emergencystatus = LOW;
  Serial.println("GPIO6 Status: OFF");
  server.send(200, "text/html", SendHTML(systemstatus,false, temperature, weight)); 
}

void handle_NotFound(){
  server.send(404, "text/plain", "Not found");
  }

void setup() {
  // initialising the Serial 
  Serial.begin(9600);
  

  //Load Cell
  scale.begin(LOADCELL_DOUT_PIN, LOADCELL_SCK_PIN);
  scale.set_scale(calibration_factor); //This value is obtained by using the SparkFun_HX711_Calibration sketch
  scale.tare(); //Assuming there is no weight on the scale at start up, reset the scale to 0

  //SD Card
  Serial.print("Initializing SD card...");
  if (!SD.begin(10)) {
  Serial.println("initialization failed!");
  while(1);
  }
  Serial.println("initialization done.");
 
   digitalWrite(LEDG,HIGH);
// rest of the board
   pinMode(2, OUTPUT);
   pinMode(LEDG, OUTPUT);
   pinMode(IGN,OUTPUT); 
   pinMode(BUZ, INPUT);

  WiFi.softAP(ssid, password);
  WiFi.softAPConfig(local_ip, gateway, subnet);
  delay(100);

  server.on("/", handle_OnConnect);
  server.on("/systemon", handle_systemon);
  server.on("/systemoff", handle_systemoff);
  server.on("/emergencyon", handle_emergencyon);
  server.on("/emergencyoff", handle_emergencyoff);
  server.onNotFound(handle_NotFound);
  server.begin();
  Serial.println("HTTP server started");
}

void loop(){
  digitalWrite(LEDG, HIGH);
  server.handleClient();
  if(systemstatus)
  {startrocketsequence();}
  if(!emergencystatus){
    digitalWrite(2,LOW);
    }
  }




void startrocketsequence() {
  for(int i=0;i<10;i++){
    digitalWrite(BUZ,HIGH);
    if(!emergencystatus){
    digitalWrite(2,LOW);
    }
    delay(500);
    digitalWrite(BUZ,LOW);
    delay(500);
  }
    
    digitalWrite(LEDG,LOW);
    digitalWrite(IGN, HIGH);   
while(true){
  if(!emergencystatus){
    digitalWrite(2,LOW);
    }
}
  weight=scale.get_units();
    Serial.print(weight, 1); //scale.get_units() returns a float
    Serial.print(" kgs"); //You can change this to kg but you'll need to refactor the calibration_factor
    Serial.print(" \t");
  
    adc_val = analogRead(thermocouple_input);
    temperature = ( ((adc_val * 4.88) - 0.0027 ) / 10.0 );
    Serial.print("Temperature = ");
    Serial.print(temperature);
    Serial.print(" \t");
   myFiletemp = SD.open("temp.csv", FILE_WRITE);
   if (myFiletemp) {
    myFiletemp.println(temperature);
    Serial.println("data updated on file");
      }else{
        Serial.println("error opening temp.csv");
   myFiletemp = SD.open("weight.csv", FILE_WRITE);
      }
   if (myFileload) {
    myFileload.println(weight);
    Serial.println("data updated on file");
      }else{
        Serial.println("error opening weight.csv");
      }
   server.send(200, "text/html", SendHTML(systemstatus,emergencystatus, temperature, weight));
  }
