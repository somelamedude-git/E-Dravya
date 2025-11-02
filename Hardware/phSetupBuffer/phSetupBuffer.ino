#include <Wire.h>
void setup() {
 Serial.begin(9600);
 Serial.println("serial monitor started");
 delay(5000);
}

void loop() {
  float buffer_arr[10];

  for(int i =0; i<10; i++){
    buffer_arr[i] = analogRead(A0);
    delay(30);
  }

  for(int i =0; i<9; i++){
    for(int j = i+1; j<10; j++){
      if(buffer_arr[i]>buffer_arr[j]){
        int temp = buffer_arr[i];
        buffer_arr[i] = buffer_arr[j];
        buffer_arr[j] = buffer_arr[i];
      }
    }
  }
  int average_value = 0;
  for(int i =1; i<=8; i++){
    float voltage = (float)buffer_arr[i]*5.0/1024/6;

    Serial.println(voltage);
    delay(1000);
  }

}
