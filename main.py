def on_received_number(receivedNumber):
    if receivedNumber == 152:
        basic.show_leds("""
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            """)
        basic.pause(100)
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            """)
        basic.pause(100)
        basic.show_leds("""
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            """)
        basic.pause(100)
        basic.clear_screen()
radio.on_received_number(on_received_number)

def on_button_pressed_a():
    global character
    character = character - 1
    basic.show_string("" + (abc[character]))
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global titkositott_szoveg, szoveg
    titkositott_szoveg = "" + titkositott_szoveg + secret[character]
    szoveg = "" + szoveg + abc[character]
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_received_string(receivedString):
    global deRecived, characterNum, convertedStr, i
    radio.send_number(152)
    deRecived = receivedString
    characterNum = len(receivedString)
    while i <= characterNum - 1:
        convertedStr = "" + convertedStr + abc[secret.index(receivedString[i])]
        i += 1
    basic.show_string(convertedStr)
radio.on_received_string(on_received_string)

def on_button_pressed_b():
    global character
    character = character + 1
    basic.show_string("" + (abc[character]))
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    radio.send_string(titkositott_szoveg)
    basic.show_leds("""
        . . . . #
        . . . # .
        # . # . .
        . # . . .
        . . . . .
        """)
    basic.pause(100)
    basic.clear_screen()
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

characterNum = 0
deRecived = ""
abc: List[str] = []
character = 0
titkositott_szoveg = ""
szoveg = ""
convertedStr = ""
i = 0
secret: List[str] = []
convertedStr = ""
radio.set_group(162)
szoveg = ""
titkositott_szoveg = ""
character = 0
abc = ["a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    " ",
    "!",
    ".",
    "?"]
secret = ["*",
    "|",
    "9",
    "Ł",
    "ß",
    "7",
    "1",
    "]",
    "%",
    "+",
    "/",
    "w",
    "\\",
    "[",
    "€",
    "o",
    "÷",
    "i",
    "{",
    "a",
    "f",
    "}",
    "Đ",
    "$",
    "&",
    "j",
    "#",
    ">",
    "6",
    "<"]
basic.show_string("" + (abc[character]))