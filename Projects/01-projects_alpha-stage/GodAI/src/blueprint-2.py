
import pyttsx3
import webbrowser
import datetime
import os
import speech_recognition as source1
print("""
                        ##############################
                     ############   God AI   ############
                        ##############################

                *    Copyright Of Captain Murlidhar Singh & ASAI Inc, 2021                 *

                *    Suggestion, Feedback & Contact E-mail; captainms.asaiinc@gmail.com    *

""")

# username
username = "Captain Skywalker"


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
    if time_in_hour > 0 and time_in_hour < 12:
        print(f'Hello {username}, Good Morning !\n')
    elif time_in_hour > 12 and time_in_hour < 16:
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
        command.pause_threshold = 1.5
        audio = command.listen(source)

    # Executing Query
    try:
        print('Recognizing...')
        query = command.recognize_google(audio, language='en-us')
        print(f"You said; {query}\n")

    except Exception as error:
        return 'None'

    return query


# Ultimate-Function
attempt = 1
if __name__ == "__main__":
    greeting()
    # logic
    while True:
        query = processCommand().lower()

        # base-commands
        # attempt-limit
        if attempt == 6:
            print("Looking Forward To Help You ...")
            speak("Looking Forward To Help You ...")
            exit()

        # intro
        elif 'who are you' in query:
            print("Hey! I'm GOD AI & I'm here to do cool tasks for you !")
            speak("I'm here to do cool tasks for you !")

        elif 'tell me about yourself' in query:
            speak(" Here's some informations about me; ")
            print("""
                        ##############################
                     ############   God AI   ############
                        ##############################

                *    Copyright Of Captain Murlidhar Singh & ASAI Inc, 2021                 *

                *    Suggestion, Feedback & Contact E-mail; captainms.asaiinc@gmail.com    *


                ######   ASAI Inc.   ######

                    *   Founder & CEO; Captain Murlidhar Singh  *

                    *   Founded On; Day 5th Of November 2020   *

                    *   ASAI Inc Stands For; an Automation System with Artificial Intelligence Incorporated    *

                    *   Origin; Earth   *


                ######   Developer & Development Details   ######

                    *   Developed Under; ASAI Inc.   *

                    *   Developed By; Captain Murlidhar Singh  (Known As; Captain Skywalker)   *

                    *   Programming Language Used; Python3 & Windows Batchfile   *

                    
                
            """)

        # feedback | work required !
        elif 'you need to improve' in query:
            print("Sure, I'll definitely improve !")
            speak("Sure...")
            exit()

        # date | work required !
        elif "the date" in query:
            speak("The Current Date is; ")
            today_date = str(os.system("date"))
            print(today_date)

        # time
        elif 'the time' in query:
            nowTime = datetime.datetime.now().strftime('%H:%M:%S')
            print(f'The time is; {nowTime}')
            speak(f'The time is; {nowTime}')

        # wishing
        elif 'good morning' in query:
            print(f'Good Morning {username}, Have a nice day !')
            speak(f'Good Morning {username}, Have a nice day !')

        elif 'good afternoon' in query:
            print(f'Good Afternoon {username}, Hope you doing a great work !')
            speak(f'Good Afternoon {username}, Hope you doing a great work !')

        elif 'good evening' in query:
            print(
                f'Good Evening {username}, It\'s time to refresh and relax for some time !')
            speak(
                f'Good Evening {username}, It\'s time to refresh and relax for some time !')

        elif 'good night' in query:
            print(f'Good Night {username}, Have a nice dream !')
            speak(f'Good Night {username}, Have a nice dream !')

        # web-commands
        # google.com
        elif 'open google.com' in query:
            webbrowser.open('https://www.google.com/')
            print('Opening Google.com...')
            speak('Opening Google.com...')
            exit()

        # duckduckgo.com
        elif "open duckduckgo" in query:
            webbrowser.open("https://duckduckgo.com/")
            print("Opening DuckDuckGo.com...")
            speak("Opening DuckDuckGo.com...")
            exit()

        # gmail.com
        elif "open gmail" in query:
            webbrowser.open("https://www.gmail.com/")
            print("Opening Google Mail...")
            speak("Opening Google Mail...")
            exit()

        # protonmail.com
        elif "open protonmail" in query:
            webbrowser.open("https://protonmail.com/")
            print("Opening ProtonMail.com...")
            speak("Opening ProtonMail.com...")
            exit()

        # blogger.com
        elif "open blogger.com" in query:
            webbrowser.open("https://www.blogger.com/")
            print("Opening Blogger.com...")
            speak("Opening Blogger.com...")
            exit()

        # youtube.com
        elif 'open youtube' in query:
            webbrowser.open('https://www.youtube.com/')
            print('Opening Youtube...')
            speak('Opening Youtube...')
            exit()

        # google drive
        elif "open google drive" in query:
            webbrowser.open("https://drive.google.com/")
            print("Opening Google Drive...")
            speak("Opening Google Drive...")
            exit()

        # google cloud shell
        elif "open cloud terminal" in query:
            webbrowser.open("https://cloud.google.com/shell/")
            print("Opening Google Cloud Shell...")
            speak("Opening Google Cloud Shell...")
            exit()

        # khanacademy.org
        elif "open khan academy" in query:
            webbrowser.open("https://www.khanacademy.org/")
            print("Opening KhanAcademy.org...")
            speak("Opening KhanAcademy.org...")
            exit()

        # udemy.com
        elif 'open udemy' in query:
            webbrowser.open('https://www.udemy.com/')
            print('Opening Udemy.com...')
            speak('Opening Udemy...')
            exit()

        # replit.com
        elif "open code browser" in query:
            webbrowser.open("https://replit.com/")
            print("Opening Replit.com...")
            speak("Opening Replit.com...")
            exit()

        # github.com
        elif 'open github' in query:
            webbrowser.open('https://github.com/')
            print('Opening Github.com...')
            speak('Opening Github...')
            exit()

        # gitlab.com
        elif "open git lab" in query:
            webbrowser.open("https://gitlab.com/")
            print("Opening GitLab...")
            speak("Opening GitLab...")
            exit()

        # docker hub
        elif "open docker hub" in query:
            webbrowser.open("https://hub.docker.com/")
            print("Opening Docker Hub...")
            speak("Opening Docker Hub...")
            exit()

        # apple.com
        elif "open apple.com" in query:
            webbrowser.open("https://www.apple.com/")
            print("Opening Apple.com...")
            speak("Opening Apple.com...")
            exit()

        # amazon.in
        elif 'open amazon.in' in query:
            webbrowser.open('https://www.amazon.in/')
            print('Opening Amazon.in...')
            speak('Opening Amazon.in...')
            exit()

        # amazon.com
        elif 'open amazon.com' in query:
            webbrowser.open('https://www.amazon.com/')
            print('Opening Amazon.com...')
            speak('Opening Amazon.com...')
            exit()

        # flipkart.com
        elif "open flipkart" in query:
            webbrowser.open("https://www.flipkart.com/")
            print("Opening Flipkart.com...")
            speak("Opening Flipkart.com...")
            exit()

        # twitter.com
        elif "open twitter" in query:
            webbrowser.open("https://twitter.com/")
            print("Opening Twitter.com...")
            speak("Opening Twitter.com...")
            exit()

        # discord.com
        elif "open discord" in query:
            webbrowser.open("https://discord.com/")
            print("Opening Discord.com...")
            speak("Opening Discord.com...")
            exit()

        # reddit.com
        elif "open reddit" in query:
            webbrowser.open("https://www.reddit.com/")
            print("Opening Reddit.com")
            speak("Opening Reddit.com")
            exit()

        # spacex.com
        elif "open space x.com" in query:
            webbrowser.open("https://www.spacex.com/")
            print("Opening SpaceX.com...")
            speak("Opening SpaceX.com...")
            exit()

        # system-commands
        # explorer
        elif "open explorer" in query:
            os.system("explorer")
            print("Opening File Explorer...")
            speak("Opening File Explorer...")
            exit()

        # files
        elif "open files" in query:
            os.system("explorer")
            print("Opening Files...")
            speak("Opening File Explorer...")
            exit()

        # bash shell
        elif "open bash shell" in query:
            print("Opening Bash Shell (Linux Terminal, WSL)...")
            speak("Opening Bash Shell...")
            os.system("bash")
            exit()

        # bash terminal
        elif "open bash terminal" in query:
            print("Opening Bash Shell (Linux Terminal, WSL)...")
            speak("Opening Bash Shell...")
            os.system("bash")
            exit()

        # kali
        elif "open kali" in query:
            print("Opening Kali Linux (Linux Terminal, WSL)...")
            speak("Opening Kali Linux...")
            os.system("kali")
            exit()

        # kali linux
        elif "open kali linux" in query:
            print("Opening Kali Linux (Linux Terminal, WSL)...")
            speak("Opening Kali Linux...")
            os.system("kali")
            exit()

        # ubuntu
        elif "open ubuntu" in query:
            print("Opening Ubuntu (Linux Terminal, WSL)...")
            speak("Opening Ubuntu...")
            os.system("ubuntu")
            exit()

        # python
        elif "open python" in query:
            print("Opening Python Shell...")
            speak("Opening Python...")
            os.system("python")
            exit()

        # vscode
        elif 'open code' in query:
            os.system("code")
            print('Opening Visual Studio Code...')
            speak('Opening VS Code...')
            exit()

        elif 'open vs code' in query:
            vscodePath = f"C:\\Users\\{username}\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(vscodePath)
            print('Opening Visual Studio Code...')
            speak('Opening VS Code...')
            exit()

        # docker desktop
        elif "open docker desktop" in query:
            docker_desktop_path = "C:\\Program Files\\Docker\\Docker\\Docker Desktop.exe"
            os.startfile(docker_desktop_path)
            print("Opening Docker Desktop...")
            speak("Opening Docker Desktop...")
            exit()

        # virtualbox
        elif "open virtualbox" in query:
            virtualbox_path = "C:\\Program Files\\Oracle\\VirtualBox\\VirtualBox.exe"
            os.startfile(virtualbox_path)
            print("Opening Virtualbox...")
            speak("Opening Virtualbox...")
            exit()

        # firefox
        elif 'open firefox' in query:
            firefox_path = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
            os.startfile(firefox_path)
            print('Opening Firefox Browser...')
            speak('Opening Firefox...')
            exit()

        # chrome
        elif "open chrome" in query:
            chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(chrome_path)
            print("Opening Chrome Browser...")
            speak("Opening Chrome...")
            exit()

        # microsoft browser
        elif "open microsoft browser" in query:
            microsoft_browser_path = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
            os.startfile(microsoft_browser_path)
            print('Opening Microsoft Edge Browser...')
            speak("Opening Microsoft Edge...")
            exit()

        # obs studio | not working ?
        elif "open obs studio" in query:
            obs_studio_path = "C:\\Program Files\\obs-studio\\bin\\64bit\\obs64.exe"
            os.startfile(obs_studio_path)
            print("Opening OBS Studio...")
            speak("Opening OBS Studio...")
            exit()

        # audacity
        elif "open audacity" in query:
            audacity_path = "C:\\Program Files (x86)\\Audacity\\audacity.exe"
            os.startfile(audacity_path)
            print("Opening Audacity...")
            speak("Opening Audacity...")
            exit()

        # control panel
        elif "open control panel" in query:
            os.system("%windir%\System32\Control.exe")
            print("Opening Control Panel...")
            speak("Opening Control Panel...")
            exit()

        # poweroff
        elif 'poweroff the system' in query:
            print('Shutting Down The System In Less Than A Minute...')
            speak('Shutting Down The System In Less Than A Minute...')
            os.system('shutdown -s')
            speak('Looking forward to help you!')
            exit()

        elif 'power of the system' in query:
            print('Shutting Down The System In Less Than A Minute...')
            speak('Shutting Down The System In Less Than A Minute...')
            os.system('shutdown -s')
            speak('Looking forward to help you...')
            exit()

        elif "stop poweroff" in query:
            print('Stoping System From Shutdown...')
            speak('Stoping System From Shutdown...')
            os.system('shutdown -a')
            speak("Welcome Back, I'm here to help you... ")

        elif "stop power of" in query:
            print('Stoping System From Shutdown...')
            speak('Stoping System From Shutdown...')
            os.system('shutdown -a')
            speak("Welcome Back, I'm here to help you... ")

        # shutdown
        elif 'shutdown the system' in query:
            print('Shutting Down The System In Less Than A Minute...')
            speak('Shutting Down The System In Less Than A Minute...')
            os.system('shutdown -s')
            speak('Looking forward to help you!')
            exit()

        elif 'shut down the system' in query:
            print('Shutting Down The System In Less Than A Minute...')
            speak('Shutting Down The System In Less Than A Minute...')
            os.system('shutdown -s')
            speak('Looking forward to help you...')
            exit()

        elif "stop shutdown" in query:
            print('Stoping System From Shutdown...')
            speak('Stoping System From Shutdown...')
            os.system('shutdown -a')
            speak("Welcome Back, I'm here to help you... ")

        elif "stop shut down" in query:
            print('Stoping System From Shutdown...')
            speak('Stoping System From Shutdown...')
            os.system('shutdown -a')
            speak("Welcome Back, I'm here to help you... ")

        # reboot
        elif 'reboot the system' in query:
            print('Rebooting The System In Less Than A Minute...')
            speak('Rebooting The System In Less Than A Minute...')
            os.system('shutdown /r')
            speak('Looking forward to help you...')
            exit()

        elif "stop reboot" in query:
            print('Stoping System From Reboot...')
            speak('Stoping System From Reboot...')
            os.system('shutdown -a')
            speak("Welcome Back, I'm here to help you... ")

        # restart
        elif 'restart the system' in query:
            print('Restarting The System In Less Than A Minute...')
            speak('Restarting The System In Less Than A Minute...')
            os.system('shutdown /r')
            speak('Looking forward to help you...')
            exit()

        elif "stop restart" in query:
            print('Stoping System From Restart...')
            speak('Stoping System From Restart...')
            os.system('shutdown -a')
            speak("Welcome Back, I'm here to help you... ")

        # Other Features;

        # base-commands;
        # exit
        elif "quit" in query:
            print("Okay !")
            speak("Okay !")
            quit()

        elif "exit" in query:
            print("Okay !")
            speak("Okay !")
            exit()

        # ok
        elif "ok" in query:
            print("Alright !")
            speak("Alright !")
            exit()

        # error-message
        else:
            print("Please! Say Again ...\n")
            speak("Say Again ...\n")
            attempt = attempt + 1
