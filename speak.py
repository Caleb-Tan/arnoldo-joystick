import sys
import pyttsx3

def speak(phrases, wpm):
    print (phrases)
    engine.setProperty("rate", wpm)
    for phrase in phrases:
        engine.say(phrase)
    engine.runAndWait() 

engine = init_engine()
print(sys.argv[1])
print(sys.argv[2])
speak(sys.argv[1].split(","), sys.argv[2])