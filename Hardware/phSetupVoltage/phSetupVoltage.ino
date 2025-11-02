#include <Arduino.h>

int phSense = A0;
int samples = 10;
float adc_resolution = 1024.0;

void setup() {
  Serial.begin(9600);
  delay(100);
}

void loop() {
  int measurings = 0;
  for(int i =0; i<samples; i++){
    measurings += analogRead(phSense);
    delay(10);
  }

  float voltage = 5/adc_resolution * measurings/samples;
  Serial.println(voltage); // Must get this to 2.5  
}
