void getObstacle() {
    bool result = digitalRead(5) == HIGH; // Read pin 5 and check if it's HIGH
    // Use the result variable as needed
    if (result == 1){
      Serial.println("NOT SECURE");
      ledAlert();
    } else {
      Serial.println("SECURE");
      displayWhite();
      delay(1500);
    }
}