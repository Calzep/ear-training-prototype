#Extensions over Dominant 7ths Ear Training
#Vesion 1.1, 02/10/2022
#By Caleb Eason, Calzep7@gmail.com

from playsound import playsound
import random
import time


#------Variable and Constants------

#A list of each root note, paired with its extensions
#0-11 represents notes in one octave starting on C

CHORDS = [('C',[1,2,3,5,6,8,9]),
          ('Db',[2,3,4,6,7,9,10]),
          ('D',[3,4,5,7,8,10,11]),
          ('Eb',[4,5,6,8,9,11,0]),
          ('E',[5,6,7,9,10,0,1]),
          ('F',[6,7,8,10,11,1,2]),
          ('Gb',[7,8,9,11,0,2,3]),
          ('G',[8,9,10,0,1,3,4]),
          ('Ab',[9,10,11,1,2,4,5]),
          ('A',[10,11,0,2,3,5,6]),
          ('Bb',[11,0,1,3,4,6,7]),
          ('B',[0,1,2,4,5,7,8])]


#A list of Chord extensions, paired with appropriate chord symbols
#EXTN is short of extension

EXTNS = [('b9','7(b9)'),
         ('9','9'),
         ('#9','7(#9)'),
         ('11','7(add11)'),
         ('#11','7(add#11)'),
         ('b13','7(addb13)'),
         ('13','7(add13)')]


#These lists contain the audio files for each chords and note

CHORDS_AUDIO = ["dominant_7ths\\C7.wav",
                "dominant_7ths\\Db7.wav",
                "dominant_7ths\\D7.wav",
                "dominant_7ths\\Eb7.wav",
                "dominant_7ths\\E7.wav",
                "dominant_7ths\\F7.wav",
                "dominant_7ths\\Gb7.wav",
                "dominant_7ths\\G7.wav",
                "dominant_7ths\\Ab7.wav",
                "dominant_7ths\\A7.wav",
                "dominant_7ths\\Bb7.wav",
                "dominant_7ths\\B7.wav"]

EXTNS_AUDIO = ["extensions\\C.wav",
               "extensions\\Db.wav",
               "extensions\\D.wav",
               "extensions\\Eb.wav",
               "extensions\\E.wav",
               "extensions\\F.wav",
               "extensions\\Gb.wav",
               "extensions\\G.wav",
               "extensions\\Ab.wav",
               "extensions\\A.wav",
               "extensions\\Bb.wav",
               "extensions\\B.wav"]


#For testing with text output as well as audio

CHORDS_TEST = ['C7','Db7','D7','Eb7','E7','F7','Gb7','G7','Ab7','A7','Bb7','B7']
EXTNS_TEST = ['C','Db','D','Eb','E','F','Gb','G','Ab','A','Bb','B']


DEMO_KEY = "demo_on" #str, password to enter text based testing mode
EXIT_DEMO_KEY = "demo_off"  #str, password to exist text based testing mode
demo_mode = False  #Boolean, determines if text outputs are displayed

REPEAT_KEY = "rep"  #str, Command used to repeat playback

PAUSE_DURATION = 2 #int/float, How long the program waits before playing the extension
 

root = 0  #int, holds a random value to determine the chord played (0-11)
extn = 0  #int, holds a random value to determine the extension played (0-6)
extn_note = 0  #int, determins what note should be played over a given chord
uinput = "null"  #Stores user input



#------Main Program------

uinput = input("Welcome to Extensions over Dominant 7ths Ear Training\nPress ENTER to start\n")

#Check if the user has entered the password for text based testing
if uinput == DEMO_KEY:
    demo_mode = True
    print("Demo mode activated!\n\n")
else:
    demo_mode = False
    
while True:
    root = random.randint(0,11)
    extn = random.randint(0,6)

    #Play Dominant Chord
    playsound(CHORDS_AUDIO[root],False)
    if demo_mode == True:
        print(CHORDS_TEST[root])
    time.sleep(PAUSE_DURATION)
    
    #Determine extension note
    extn_note = CHORDS[root][1][extn]
    #Play Extension
    playsound(EXTNS_AUDIO[extn_note],False)
    if demo_mode == True:
        print(EXTNS_TEST[extn_note])

    #User Input Phase
    while True:
        uinput = input("\n\nWhat extension was played?\n")
        #Validate user input
        if any(uinput in i for i in EXTNS):
            break
        elif uinput == REPEAT_KEY:
            playsound(CHORDS_AUDIO[root],False)
            time.sleep(PAUSE_DURATION)
            playsound(EXTNS_AUDIO[extn_note],False)
        else:
            print("Invalid input!  Accepted inputs:")
            for i in EXTNS:
                print(i[0])
            
    #Mark answer
    if uinput == EXTNS[extn][0]:
        print("\nCorrect!\nThe chord played was",str(CHORDS[root][0])+str(EXTNS[extn][1]))
    else:
        print("\nIncorrect.\nThe chord played was",str(CHORDS[root][0])+str(EXTNS[extn][1]))

    uinput = input("Press ENTER to continue\n")
    if uinput == DEMO_KEY:
        demo_mode = True
        print("Demo mode activated!\n")
    elif uinput == EXIT_DEMO_KEY:
        demo_mode = False
        print("Demo mode deactivated!\n")
