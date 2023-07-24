import datetime
import os
import smtplib
import webbrowser
import pyttsx3
import speech_recognition as sr
import pyaudio
import wikipedia
import random
import pywhatkit
import requests
import pyjokes


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir")

    else:
        speak("Good Evening sir")

    speak("I am Jarvis, How may I help you")


def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("liddtnrning")
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        # speak("You said")
        # speak(query)

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query.lower()

def myLocation():
    ip_add = requests.get('https://api.ipify.org').text

    url = 'https://get.geojs.io/v1/ip/geo/' + ip_add + '.json'

    geo_r = requests.get(url)

    geo_d = geo_r.json()

    state = geo_d['city']

    country = geo_d['country']

    speak(f"Sir, you are in {state , country} .")


if __name__ == '__main__':
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()


#SEARCH ON WIKIPEDIA#
        if 'wikipedia' in query:
            speak("Searching wikipedia...")
            query = query.replace("wikipedia", " ")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)

        elif 'who is' in query:
            speak("Searching on wikipedia...")
            query = query.replace("who is", " ")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)

        # elif '' in query:
        #     speak("What do yuo want to say?")

# finding my Current location

        elif 'my location' in query:
            myLocation()


#OPEN WEBSITES USING WEBBROWSER MODULE

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak("Opening Youtube")

        elif 'open google' in query:
            webbrowser.open("google.com")
            speak("Opening google")

        elif 'open instagram' in query:
            webbrowser.open("instagram.com")
            speak("Opening instagram")

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")
            speak("Opening facebook")

        elif 'open whatsapp' in query:
            webbrowser.open("web.whatsapp.com")
            speak("Opening whatsapp")


        elif 'stack overflow' in query:
            webbrowser.open("stackoverflow.com")
            speak("Opening stackoverflow")

        elif 'open gmail' in query:
            webbrowser.open("gmail.com")
            speak("Opening gmail")

        elif 'open Tenserflow' in query:
            webbrowser.open("tenserflow.com")
            speak("Opening tenserflow")

        elif 'open telegram' in query:
            webbrowser.open("telegram.com")
            speak("Opening telegram")

        elif 'open python' in query:
            webbrowser.open('https://www.python.org/')
            speak("opening python")


# To find a joke
        elif 'tell me a joke' in query:
            joke = pyjokes.get_joke()
            print(joke)
            speak(joke)

        

#ASK JARVIS DATE AND TIME#
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%I:%M %p")
            print(strTime)
            speak(f"Sir, the time is {strTime}")

        elif 'date' in query:
            strDate = datetime.datetime.now().strftime("%m-%d-%Y")
            print(strDate)
            speak(f"Sir, todays date is {strDate}")


#OPENING DESKTOP APPLICATIONS#

        elif 'open code' in query:
            codePath = "C:\\Users\\jayen\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            speak("opening code")

        elif 'open excel' in query:
            excelPath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.exe"
            os.startfile(excelPath)
            speak("opening Excel")

        elif 'open chrome' in query:
            chromePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(chromePath)
            speak("opening chrome")

        elif 'open notepad' in query:
            notePath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Notepad"
            os.startfile(notePath)
            speak("opening notePad")

        elif 'open wordpad' in query:
            wordPath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\WordPad"
            os.startfile(wordPath)
            speak("opening wordPad")

        elif 'open snipping tool' in query:
            snip = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Snipping Tool"
            os.startfile(snip)
            speak("opening snipping Tool")

        

        elif 'open powershel' in query:
            powerPath = "C:\\Users\\jayen\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Windows PowerShell\\Windows PowerShell"
            os.startfile(powerPath)
            speak("opening powershel window")

        elif 'open command prompt' in query:
            os.system("start cmd")

        elif 'open pycharm' in query:
            pychrm = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2021.2.1\\bin\\pycharm64.exe"
            os.startfile(pychrm)
            speak("opening pycharm")

        elif 'open autocad' in query:
            autoPath = "C:\\Program Files\\Autodesk\\AutoCAD 2022\\acad.exe"
            os.startfile(autoPath)
            speak("opening Autodesk Autocad")

        elif 'open settings' in query:
            SettingPath = "%windir%\\System32\\Control.exe"
            os.startfile(SettingPath)
            speak("opening Settings")

        elif 'open Paint' in query:
            paintPath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Paint"
            os.startfile(paintPath)
            speak("opening Paint")

        elif 'open task manager' in query:
            taskPath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Task Manager"
            os.startfile(taskPath)
            speak("opening Task Manager")


#To close or kill the opened tasks
        elif 'close notepad' in query:
            speak("Okay sir, closing notepad")
            os.system("taskkill /f /im notepad.exe")

        elif 'close excel' in query:
            speak("Okay sir, closing Excel")
            os.system("taskkill /f /im Excel.exe")

        elif 'close pycharm' in query:
            speak("Okay sir, closing Pycharm")
            os.system("taskkill /f /im pycharm.exe")

        elif 'close powershell' in query:
            speak("Okay sir, closing powershell")
            os.system("taskkill /f /im powershell.exe")

        elif 'close command prompt' in query:
            speak("Okay sir, closing command prompt")
            os.system("taskkill /f /im cmd.exe")

        
        elif 'close autocad' in query:
            speak("Okay sir, closing autocad")
            os.system("taskkill /f /im acad.exe")

        # elif 'close task manager' in query:
        #     speak("Okay sir, closing task manager")
        #     os.system("taskkill /f /im Task Manager.exe")



        # elif 'play music' in query:
        #     n = random.choice(0)
        #     print(n)
        #     music_dir = 'C:\\gj\\music'
        #     songs = os.listdir(music_dir)
        #     # speak("Which song do you want to play")
        #     os.startfile(os.path.join(music_dir, songs[n]))
        #     print(songs)

#PLAY SONGS ON YOUTUBE#
        elif 'play' in query:
            yt = query.replace('youtube', '')
            yt = query.replace('play', '')
            speak('Playing' + yt)
            pywhatkit.playonyt(yt)


#To set an alarm

        elif 'set alarm' in query:
            speak("please Enter the time !")
            time = input("please Enter the time :")

            while True:
                alarm = datetime.datetime.now()
                now = alarm.strftime("%H:%M:%S")

                if now == time:
                    os.startfile('Khudko.mp3')
                    speak("Its time to wake up Sir")
                    speak("alarm closed")


                elif now>time:
                    break

#greeting messages
        elif 'thank you' in query:
            speak("Most welcome sir, It's my pleasure")

        elif 'hate you' in query:
            speak("sorry sir, have I did some mistake")

        elif 'love you' in query:
            speak("I love You too dear")

        elif 'help me' in query:
            speak("Off course, I am always be there to help you")

        elif 'how are you' in query:
            speak("I am fine sir, what about you")

        elif 'I am fine' in query:
            speak("Thats great, Happy to hear that")

        elif 'hello Jarvis' in query:
            speak("Hello sir", 'wishMe')


        
#System restart , Shut down , Sleep

        elif 'restart the system' in query:
            speak("coming back soon")
            os.system("shutdown /r /t 5")

        elif 'shut down the system' in query:
            speak("good bye sir")
            os.system("shutdown /s /t 5")

        elif 'sleep the system' in query:
            os.system("rundll32.exe powrprof.dll, SetupSuspendState 0,1,0")
        

#jARVIS WILL GO TO SLEEP/exit#
        elif 'exit' in query:
            speak("Quiting Jarvis, Thank you sir")
            exit()

        elif 'shut down' in query:
            speak("Shutting down, good bye Sir")
            exit()

        elif 'quit' in query:
            speak("Quiting Jarvis, Thank you sir, Good bye")
            exit()

        if 'you need a break' in query:
            speak("Ok sir, you can call me any time!")
            sys.exit()

        elif 'sleep now' in query:
            speak("Ok sir, I am going to sleep, Take care")
            exit()

