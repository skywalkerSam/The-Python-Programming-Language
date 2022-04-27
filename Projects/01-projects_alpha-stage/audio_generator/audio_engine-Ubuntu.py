
# Workstation; Ubuntu 20.04
    #-> Also implemented in God-AI which also runs on windows10

'''
# Dependencies;

-> Install espeak ffmpeg

-> pip3 install pyttsx3
    # pyttsx3 documentation; https://pypi.org/project/pyttsx3/

'''

# Welcome screen
print("""

                     Text To Audio Generator

""")


import pyttsx3

# voice_engine
voice_engine = pyttsx3.init('espeak')   # object creation, voice_engine
# voice_engine.say('Hello World')

# voice_engine_voice
voice_engine_voice = voice_engine.getProperty('voices')
# print(voices[11].id)
voice_engine.setProperty('voice', voice_engine_voice[11].id)

# voice_engine_rate
voice_engine_rate = voice_engine.getProperty('rate')
# print(voice_engine_rate)
voice_engine.setProperty('rate', 180)

# voice_engine_volume
voice_engine_volume = voice_engine.getProperty('voice')
# print(voice_engine_volume)
# voice_engine.setProperty('voice', 1.0)


textfile = str(input('Enter Text; '))

filedestination = input('Enter File Destination,  (Ex:- /home/username/folder/filename.mp3) ; \n')


# Saving voice to a file
# voice_engine.say(textfile)
voice_engine.save_to_file(textfile, filedestination )
voice_engine.runAndWait()

