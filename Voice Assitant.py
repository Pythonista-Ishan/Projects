import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import pyjokes
from bs4 import BeautifulSoup 
import subprocess

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir!")   

    else:
        speak("Good Evening Sir!")  

    speak("I am Caroline . Please tell me how may I help you")       

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)    
        print("Say that again please...")  
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("opening youtube")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("opening google")
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            speak("opening stackflow")
            webbrowser.open("stackoverflow.com")

        elif 'open twitter' in query:
            speak("opening twitter")
            webbrowser.open("twitter.com")

        elif 'open facebook' in query:
            speak("opening facebook")
            webbrowser.open("facebook.com")

        elif 'news' in query:
            speak("opening news")
            webbrowser.open("news.google.com")

        elif 'play music' in query or 'play song' in query:
            music_dir = 'E:\\music'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            speak("opening visual studio code")
            codePath = "C:\\Users\\91752\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        
        elif 'bye' in query or 'quit' in query or 'exit' in query:
            speak("goodbye and have a nice day")
            break
    
        elif 'who are you' in query:
            speak("I am an assistant designed on the python as a project. My name is based on the character of one of the most famous and popular show 'THE VAMPIRE DIARIES'. I am designed for performing some basic tasks of regular days. I hope you will find me interesting. ")

        elif 'how are you' in query:
            speak("I am good sir. how are you")

        elif 'fine' in query:
            speak("that's great sir, stay safe during this pendamic. Tell me how may i help you")

        elif 'joke' in query:
            speak(pyjokes.get_joke())

        elif 'search' in query:
            query = query.replace("search", "")
            webbrowser.open(query)
