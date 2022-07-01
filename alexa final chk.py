import webbrowser
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import os
import wikipedia

listener = sr.Recognizer()
engine = pyttsx3.init()
rate = engine.setProperty("rate",150)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            #listener.listen(source, None, 3)
            talk("listening")
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice,language='en')
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command

def run_alexa():
    command = take_command()
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print('Current time is ' + time)
        talk('Current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'your developer' in command:
        print('Mr.Tahir Habib is my developer.')
        talk('Mister Tahir Habib is my developer.')
    elif 'how are you' in command:
        print('I am good sir!')
        talk('I am good sir!')
    elif "what is" in command:
        thing = command.replace('alexa what is', '')
        information = wikipedia.summary(thing, 2)
        print(information)
        talk(information)

    elif 'who is' in command:
        person = command.replace("who is", '')
        info = wikipedia.summary(person, 2)
        print(info)
        talk(info)
    elif 'your developer' in command:
        print("Mr.Tahir Habib is my developer.")
        talk("Mister Tahir Habib is my developer!")
    elif 'google' in command:
        print("What would like you search on Google?")
        talk("What would like you search on Google!")
        command_google = take_command()
        webbrowser.open("https://www.google.com/search?q="+"".join(command_google))
    elif 'my university website' in command:
        print('opening your university website...')
        talk("opening your university website!")
        webbrowser.open('iub.edu.pk')

    elif 'youtube' in command:
        print("What would like you search on Youtube?")
        talk("What would like you search on Youtube!")
        command_youtube = take_command()
        webbrowser.open("https://www.youtube.com/" + "+".join(command_youtube))

    elif 'how are you' in command:
        print("I am fine sir!")
        talk("I am fine sir!")
    elif 'open pycharm' in command:
        print("Opening Pycharm...")
        talk("opening Pycharm!")
        pycharm_code = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2021.2.1\\bin\\pycharm64.exe"
        os.startfile(pycharm_code)
    elif 'open ms word' in command:
        print("Opening MS word... ")
        talk("opening MS word!")
        MS_word_code = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
        os.startfile(MS_word_code)
    elif 'open powerpoint' in command:
        print("Opening Power Point... ")
        talk("opening Power Point")
        ppt_code = "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
        os.startfile(ppt_code)
    elif 'open excel' in command:
        print("Opening Excel... ")
        talk("opening Excel")
        excel_code = "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"
        os.startfile(excel_code)
    elif 'quit' or 'exit' or 'good bye' in command:
        exit()
    print(command)



while True:
    run_alexa()
