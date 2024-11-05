let sensorValue = 0
// Set a threshold value for smoke detection
let threshold = 460
// Set a threshold value for smoke detection
basic.forever(function () {
    // Read the analog value from MQ-7
    sensorValue = pins.analogReadPin(AnalogPin.P0)
    if (sensorValue > threshold) {
        // If smoke is detected
        // Show a sad face
        basic.showIcon(IconNames.Sad)
        // Continuously beep while smoke is detected
        while (sensorValue > threshold) {
            // Beep the alarm
            music.playTone(262, music.beat(BeatFraction.Quarter))
            // Adjust pause duration for beep frequency
            basic.pause(100)
            // Re-read the sensor value
            sensorValue = pins.analogReadPin(AnalogPin.P0)
        }
    } else {
        // If no smoke is detected
        // Clear the screen before showing the happy face
        basic.clearScreen()
        // Show a happy face
        basic.showIcon(IconNames.Happy)
        // Stop any sound that is currently playing
        music.stopAllSounds()
    }
    // Wait for half a second before the next reading
    basic.pause(500)
})
