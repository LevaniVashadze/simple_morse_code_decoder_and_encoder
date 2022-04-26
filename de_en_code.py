class Morse:
    def __init__(self):
        self.morse = {
                          "0": "-----",
                          "1": ".----",
                          "2": "..---",
                          "3": "...--",
                          "4": "....-",
                          "5": ".....",
                          "6": "-....",
                          "7": "--...",
                          "8": "---..",
                          "9": "----.",
                          "a": ".-",
                          "b": "-...",
                          "c": "-.-.",
                          "d": "-..",
                          "e": ".",
                          "f": "..-.",
                          "g": "--.",
                          "h": "....",
                          "i": "..",
                          "j": ".---",
                          "k": "-.-",
                          "l": ".-..",
                          "m": "--",
                          "n": "-.",
                          "o": "---",
                          "p": ".--.",
                          "q": "--.-",
                          "r": ".-.",
                          "s": "...",
                          "t": "-",
                          "u": "..-",
                          "v": "...-",
                          "w": ".--",
                          "x": "-..-",
                          "y": "-.--",
                          "z": "--..",
                          ".": ".-.-.-",
                          ",": "--..--",
                          "?": "..--..",
                          "!": "-.-.--",
                          "-": "-....-",
                          "/": "-..-.",
                          "@": ".--.-.",
                          "(": "-.--.",
                          ")": "-.--.-"
                        }

    def encode(self, string):
        encoded_list = []

        for char in string:

            for key in self.morse:
                if key == char.lower():
                    encoded_list.append(self.morse[key])

        encoded_string = ' '.join(encoded_list)
        return encoded_string

    def decode(self, string):
        decoded_list = []
        morse_list = string.split()

        for item in morse_list:

            for key, value in self.morse.items():
                if value == item:
                    decoded_list.append(key)

        decoded_string = ''.join(decoded_list)
        return decoded_string
