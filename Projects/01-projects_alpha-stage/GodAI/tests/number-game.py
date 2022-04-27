
print("""
                        ##############################
                     ############   God AI   ############
                        ##############################

                *    Copyright Of Captain Murlidhar Singh & ASAI Inc, 2021                 *

                *    Suggestion, Feedback & Contact E-mail; captainms.asaiinc@gmail.com    *

""")

#username
username = "Captain Skywalker"


#modules_required
import pyttsx3 
import datetime  
import speech_recognition as source1
import random


# voice_engine
voice_engine = pyttsx3.init('sapi5')   # object creation, voice_engine
# voice_engine.say('Hello World')

# voice_engine_voice
voice_engine_voice = voice_engine.getProperty('voices')
# print(voice_engine_voice[1].id)
voice_engine.setProperty('voice', voice_engine_voice[1].id)

# voice_engine_rate
voice_engine_rate = voice_engine.getProperty('rate')
# print(voice_engine_rate)
voice_engine.setProperty('rate', 210)


def speak(audio):   # A speak function(), which takes audio as it's parameter
    voice_engine.say(audio)
    voice_engine.runAndWait()
    

# Greeting message
def greeting():
    time1 = datetime.datetime.now()
    # print(time1)
    time_in_hour = int(datetime.datetime.now().hour)
    # print(time_in_hour)
    if time_in_hour>0 and time_in_hour<12:
        print(f'Hello {username}, Good Morning !\n')
    elif time_in_hour>12 and time_in_hour<16:
        print(f'Hello {username}, Good Afternoon !\n')
    else:
        print(f'Hello {username}, Good Evening !\n')

    print("I'm here to help you :)")   # Ultimate statements
    speak("I'm here to help you ... ")   


def processCommand():
    """
    It processes voice command from microphone & returns result of the command !        
    """
    command = source1.Recognizer()
    with source1.Microphone() as source:
        print("Listening...")
        command.pause_threshold=1.5      
        audio = command.listen(source)

    #Executing Query
    try:
        print('Recognizing...')
        query = command.recognize_google(audio, language='en-us')
        print(f"You said; {query}\n")

    except Exception as error:
        return 'None'

    return query


#Ultimate Function()
attempt = 1
if __name__ == "__main__":
    greeting()
    #logic
    while True:
        query = processCommand().lower()
        if attempt == 6:
            print("Looking Forward To Help You ...")
            speak("Looking Forward To Help You ...")
            exit()




        #number game
        elif 'open number game' or "start number game" in query:  
            print('Starting Guess The Number Game...')
            speak('Starting Guess The Number Game...')          
            print("""
                            ##############################
                        ######       Number Game        ######   
                            ##############################

                        *   Developed Under; ASAI Inc.    *

                        *   Developed By; Captain Murlidhar Singh   *
            
            """) 
            player_name = input('Enter Your Name; ')
            print('\nHello ', player_name.capitalize(),'!')
            speak('Read the rules carefully')
            print("""
                    GAME RULES;
                    1. You Have 10 Attempts Only
                    2. The Number Should Must Between 3 to 33

                    TIPS;
                    1. [ > ] = Greater Than
                    2. [ < ] = Less Than
            
            """)
            speak(f'Now, Guess The Number {player_name}')
            print('Now, Guess The Number', player_name.capitalize(),"; ")

            #logic
            number = random.randint(3, 33)
            # print(number)
            user_attempt = 1
            while(user_attempt <= 10):
                player_responce = int(input())

                if player_responce < 3:
                    print("Enter number greater than 3")
                    speak("Read the rules carefully")

                elif player_responce > 33:
                    print("Enter number smaller than 33")
                    speak("Read the rules carefully")

                elif player_responce > number:
                    print('Enter Smaller Number; ')
                    speak('Enter Smaller Number')

                elif player_responce < number:
                    print('Enter Greater number; ')
                    speak('Enter Greater number')

                elif player_responce == number + 5 or player_responce == number - 5:
                    print("You are almost there, enter number; ")
                    speak("You are almost there, enter number; ")

                elif player_responce == number:
                    print('You Won, Conratulations !')
                    speak('You Won, Conratulations !')
                    exit()

                else:
                    print('Read The Rules Carefully & Try Again!')
                    speak('Read The Rules Carefully & Try Again!')

                print(10 - user_attempt, 'Attempt Left!')
                user_attempt = user_attempt+1

            if user_attempt > 9:
                print('Game Over!\nThanks For Playing!\n')
                speak("Game Over")
                exit()







        elif "quit" in query:
            print("Okay !")
            speak("Okay !")
            quit()

        elif "exit" in query:
            print("Okay !")
            speak("Okay !")
            exit()

        elif "ok" in query:
            print("Alright !")
            speak("Alright !")
            exit()

        else:
            print("Please! Say Again ...\n")
            speak("Say Again ...\n")
            attempt = attempt + 1












