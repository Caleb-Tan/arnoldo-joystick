from espeak import espeak
import threading
import time
import wordninja

class Tts:
    code = [["A", "B", "C", "D", "E"],
            ["F", "G", "H", "I", "J"],
            ["L", "M", "N", "O", "P"],
            ["Q", "R", "S", "T", "U"],
            ["V", "W", "X", "Y", "Z"]]

    def __init__(self):
        self.sentence = ""
        self.current_row = -1
        espeak.set_parameter(1,90)
        espeak.set_voice("en-us")
        
    def select_row(self, key):
        self.current_row = key
        espeak.set_parameter(1, 110)
        self.speak(self.code[key][0])
        self.speak(" too ")
        self.speak(self.code[key][4])
        espeak.set_parameter(1,60)

    def select_letter(self, key):
        letter = self.code[self.current_row][key]
        self.current_row = -1
        self.sentence += letter
        self.speak(letter)
        
    def play_sentence(self):
        sentence = " ".join(wordninja.split(self.sentence))
        self.speak(sentence)
        self.sentence = ""
        self.current_row = -1

    '''
    0-4 = rows/letters
    5 = speak sentence
    6 = go back
    '''
    def handle_action(self, key):
        if key == 5:
            self.play_sentence()
        elif key == 6:
            pass
        else:
            if self.current_row == -1:
                self.select_row(key)
            else:
                self.select_letter(key)
    
    def speak(self, sentence):
        espeak.synth(sentence)



