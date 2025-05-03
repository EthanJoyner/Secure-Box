// PIR Motion Sensor Code
// Connect the PIR sensor output to pin 4
void checkMotion() {
    const int pirPin = 4; // PIR sensor output pin
    int motionDetected = 0; // Variable to store motion status
    pinMode(pirPin, INPUT); // Set PIR pin as input
    motionDetected = digitalRead(pirPin); // Read PIR sensor state

    if (motionDetected == HIGH) {
        Serial.println("Motion True");
        displayWhite();
    } else {
        Serial.println("Motion False");
        ledOff();
    }

    delay(100); // Delay to avoid spamming the serial monitor
}