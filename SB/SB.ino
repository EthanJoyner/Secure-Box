void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}
char signal;

void loop() {
  // if (Serial.available() > 0 ){
  //   signal = Serial.read();
  //   Serial.println(signal);
  //   if (signal == 'm'){
  //     checkMotion();
  //   } else if (signal == 'o'){
  //     getObstacle();
  //   } else {
  //     checkMotion();
  //   }
    
  // }
  getObstacle();
  checkMotion();

}
