import sys
import pyttsx3

def speak(phrases, wpm):
    print (phrases)
    engine.setProperty("rate", wpm)
    for phrase in phrases:
        engine.say(phrase)
    engine.runAndWait() 

engine = init_engine()
speak(sys.argv[1], sys.argv[2])