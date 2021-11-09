# import tts
import pyttsx3
engine = pyttsx3.init()

# main function
def beer_on_wall():
    for x in reversed(range(1, 100)):
        
        if x > 1:
            print(x, 'bottles of beer on the wall')
            engine.say(x)
            engine.say('bottles of beer on the wall')
            engine.runAndWait()
        elif x == 1:
            print(x, 'bottle of beer on the wall')
            engine.say(x)
            engine.say('bottle of beer on the wall')
            engine.runAndWait()
    else:
        print('No bottles of beer on the wall…. Go to the store and buy some more…')
        engine.say('No bottles of beer on the wall…. Go to the store and buy some more…')
        engine.runAndWait()
        beer_on_wall()

beer_on_wall()