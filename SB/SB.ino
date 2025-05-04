void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(A0, OUTPUT);
  digitalWrite(A0, HIGH);
}
char signal;

void loop() {
  
  getObstacle();
}
