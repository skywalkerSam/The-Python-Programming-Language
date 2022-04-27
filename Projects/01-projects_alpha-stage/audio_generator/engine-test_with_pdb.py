"""
Developer: Starboy  
Purpose: Text to audio generator for Windows systems
Date: 12022.04.04.17:29
"""

from pyfiglet import figlet_format
import pyttsx3
import pdb


while(True):
    try:
        # pdb.set_trace()
        def audio_generator():
            print(figlet_format("\n Audio Generator", "small"))
            # Audio Engine
            audio_engine = pyttsx3.init('sapi5')
            audio_engine_voice = audio_engine.getProperty('voices')
            audio_engine.setProperty(
                'voice', audio_engine_voice[1].id)     # Cortana's voice
            # Voice Speed
            audio_engine.getProperty('rate')
            audio_engine.setProperty('rate', 200)

            # Speak function
            def speak(text):
                audio_engine.say(text)
                audio_engine.runAndWait()

            # File Processing
            speak("Please enter some text")
            text_file = str(input('Enter Text: '))
            speak("Now, enter the filename with its type and its destination")
            audio_file = input("\n Enter Filename With Its Type (.mp3) & It's Destination (D:/Music/hello.mp3): \n\n\t")
            audio_engine.save_to_file(text_file, audio_file)
            audio_engine.runAndWait()

        if __name__ == "__main__":
            audio_generator()
            continue

    except KeyboardInterrupt:
        print("\n\n\t Operation Cancelled By User :( \n")
        break

    except:
        print("Something Went Wrong, Try Again!")
        continue



"""
Conclusion:
    - I was able to find the problem with pdb, yes!

Problem Definition:
    - The cortana's voice index for the engine's audio was out of range in my windows 11 pc.
    - For me:
             audio_engine.setProperty(
                'voice', audio_engine_voice[1].id)     # Cortana's voice
"""
