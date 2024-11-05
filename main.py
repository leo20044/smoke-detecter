input.onButtonPressed(Button.A, function () {
    basic.showString(".")
    // Add dot to current Morse sequence
    morseLetter = "" + morseLetter + "."
})
// Shake to indicate the end of a word
input.onGesture(Gesture.LogoUp, function () {
    // Space to indicate end of word
    radio.sendString(" ")
    basic.clearScreen()
})
// A+B button press sends the current Morse sequence as a letter
input.onButtonPressed(Button.AB, function () {
    // Transmit Morse sequence for letter
    radio.sendString(morseLetter)
    // Clear sequence for next letter
    morseLetter = ""
})
radio.onReceivedString(function (receivedString) {
    if (receivedString == " ") {
        // End of word: Show a space between words
        basic.showString(" ")
    } else {
        // End of letter: Decode and display it
        if (morseDictionary[0]) {
            basic.showString("" + (morseDictionary[0]))
        } else {
            // Show ? if code is not in dictionary
            basic.showString("?")
        }
    }
})
input.onButtonPressed(Button.B, function () {
    basic.showString("-")
    // Add dash to current Morse sequence
    morseLetter = "" + morseLetter + "-"
})
let morseLetter = ""
let morseCode = ""
radio.setGroup(1)
let morseDictionary: { [key: string]: string } = {
    ".-": "A", "-...": "B", "-.-.": "C", "-..": "D",
    ".": "E", "..-.": "F", "--.": "G", "....": "H",
    "..": "I", ".---": "J", "-.-": "K", ".-..": "L",
    "--": "M", "-.": "N", "---": "O", ".--.": "P",
    "--.-": "Q", ".-.": "R", "...": "S", "-": "T",
    "..-": "U", "...-": "V", ".--": "W", "-..-": "X",
    "-.--": "Y", "--..": "Z"
};
radio.setGroup(1)
