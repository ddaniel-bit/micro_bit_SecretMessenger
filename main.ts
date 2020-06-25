radio.onReceivedNumber(function (receivedNumber) {
    if (receivedNumber == 152) {
        basic.showLeds(`
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            `)
        basic.pause(100)
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            `)
        basic.pause(100)
        basic.showLeds(`
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            `)
        basic.pause(100)
        basic.clearScreen()
    }
})
input.onButtonPressed(Button.A, function () {
    character = character - 1
    basic.showString("" + (abc[character]))
})
input.onButtonPressed(Button.AB, function () {
    titkositott_szoveg = "" + titkositott_szoveg + secret[character]
    szoveg = "" + szoveg + abc[character]
})
radio.onReceivedString(function (receivedString) {
    radio.sendNumber(152)
    deRecived = receivedString
    characterNum = receivedString.length
    while (i <= characterNum - 1) {
        convertedStr = "" + convertedStr + abc[_py.py_array_index(secret, receivedString[i])]
        i += 1
    }
    basic.showString(convertedStr)
})
input.onButtonPressed(Button.B, function () {
    character = character + 1
    basic.showString("" + (abc[character]))
})
input.onGesture(Gesture.Shake, function () {
    radio.sendString(titkositott_szoveg)
    basic.showLeds(`
        . . . . #
        . . . # .
        # . # . .
        . # . . .
        . . . . .
        `)
    basic.pause(100)
    basic.clearScreen()
})
let characterNum = 0
let deRecived = ""
let abc: string[] = []
let character = 0
let titkositott_szoveg = ""
let szoveg = ""
let convertedStr = ""
let i = 0
let secret : string[] = []
convertedStr = ""
radio.setGroup(162)
szoveg = ""
titkositott_szoveg = ""
character = 0
abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " ", "!", ".", "?"]
secret = ["*", "|", "9", "Ł", "ß", "7", "1", "]", "%", "+", "/", "w", "\\", "[", "€", "o", "÷", "i", "{", "a", "f", "}", "Đ", "$", "&", "j", "#", ">", "6", "<"]
basic.showString("by:ddaniel-bit")
basic.showString("" + (abc[character]))
