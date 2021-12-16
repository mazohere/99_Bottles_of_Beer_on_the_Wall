# import tts
import pyttsx3
engine = pyttsx3.init()

# main function
def beer_on_wall():

    # iteratively counts up from 100 
    for x in reversed(range(1, 100)):
        
        # prints x amount of bottles of beer on the wall for as long as x > 1, when x = 1 prints 1 bottle of beer on the wall,
        # this is for grammar reasons
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
    # loops when the function ends by printing the end of the song and re-calling the function
    else:
        print('No bottles of beer on the wall…. Go to the store and buy some more…')
        engine.say('No bottles of beer on the wall…. Go to the store and buy some more…')
        engine.runAndWait()
        beer_on_wall()

beer_on_wall()