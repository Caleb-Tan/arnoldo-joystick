import pyttsx3
engine = pyttsx3.init() # object creation

""" RATE"""
engine.setProperty('rate', 125)     # setting up new voice rate


"""VOLUME"""
engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1

"""VOICE"""
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

engine.say("Hello World!")
engine.say('My current speaking rate is ' + str(rate))
engine.runAndWait()
engine.stop()