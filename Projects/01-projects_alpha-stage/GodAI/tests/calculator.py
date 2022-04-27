

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


        #calculator
        elif "open calculator" in query:
            speak('Opening Calculator...')
            print('Opening Calculator...')
            print("""
                        ##############################
                    ######   The Basic Calculator   ######
                        ##############################

                    *   Developed Under; ASAI Inc.    *

                    *   Developed By; Captain Murlidhar Singh   *
            
            """)  
            speak(" Welcome to THE BASIC CALCULATOR ! ") 

            print('Enter The First Number;')
            speak('Enter The First Number')
            num1=int(input())

            print('Enter The Operation [+, -, *, /, //, %, ]; ')
            speak('Now, Enter The Operation, which you wanna do ')
            operator=input()

            print('Enter The Second Number; ')
            speak('Now, Enter The Second Number')
            num2=int(input())

            if operator=='+':
                speak("Here's Your Answer")
                print('The answer of your given operation; ', num1+num2)
                print('\nTHANKS FOR COMING!')
                speak('Thanks For Coming!')
                exit()

            elif operator=='-':
                speak("Here's Your Answer")
                print('The answer of your given operation; ', num1-num2)
                print('\nTHANKS FOR COMING!')
                speak('Thanks For Coming!')
                exit()

            elif operator=='*':
                speak("Here's Your Answer")
                print('The answer of your given operation; ', num1*num2)
                print('\nTHANKS FOR COMING!')
                speak('Thanks For Coming!')
                exit()

            elif operator=='**':            
                speak("Here's Your Answer")
                print('The answer of your given operation; ', num1**num2)
                print('\nTHANKS FOR COMING!')
                speak('Thanks For Coming!')
                exit()

            elif operator=='/':
                speak("Here's Your Answer")
                print('The answer of your given operation; ', num1/num2)
                print('\nTHANKS FOR COMING!')
                speak('Thanks For Coming!')
                exit()

            elif operator=='//':
                speak("Here's Your Answer")
                print('The answer of your given operation; ', num1//num2)
                print('\nTHANKS FOR COMING!')
                speak('Thanks For Coming!')
                exit()

            elif operator=='%':
                speak("Here's Your Answer")
                print('The answer of your given operation; ', num1%num2)
                print('\nTHANKS FOR COMING!')
                speak('Thanks For Coming!')
                exit()

            else:
                print('Enter a valid Operation!')
                speak('Enter a valid Operation!')
                print('\nTHANKS FOR COMING!')
                speak('Thanks For Coming!')
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



























