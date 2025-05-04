// Passive Piezo Buzzer Example
// This code generates a simple tone on a passive piezo buzzer.
void piezoGo() {
    const int piezoPin = 7; // Pin connected to the piezo buzzer
    pinMode(piezoPin, OUTPUT); // Set the piezo pin as an output
    // Play a tone at 1000 Hz for 500 ms
    digitalWrite(piezoPin, HIGH); // Turn on the buzzer
    delay(100); // Wait for 1 second before playing the tone again
    digitalWrite(piezoPin, LOW); // Turn on the buzzer
}