import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pywhatkit
import webbrowser
import playsound
import os
import random
import time
import subprocess
import winshell
import gtts
import wolframalpha
import operator
from ecapture import ecapture as ec
from twilio.rest import Client
from datetime import date
from playsound import playsound
from gtts import gTTS
from selenium import webdriver
from time import sleep
from pyyoutube import Api
import json
import requests
import pyjokes

print('Hello i am your Voice Assistant')
engine=pyttsx3.init()
voices=engine.getProperty('voices')
#engine.setProperty('voice',voices[0].id)
engine.setProperty('voice',voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Good Morning ")
        print("Good Morning ")
    elif hour>=12 and hour<18:
        speak("Good Afternoon ")
        print("Good Afternoon")
    else:
        speak("Good Evening")
        print("Good Evening")

def note(statement):
    date = datetime.datetime.now()
    file_name = str(date).replace(":", "-") + "-note.txt"
    with open(file_name, "w") as f:
        f.write(statement)
    subprocess.Popen(["notepad.exe", file_name])

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)

        try:
            statement=r.recognize_google(audio,language='en-in')
            print(f"user said:{statement}\n")

        except Exception as e:
            speak("Pardon me please")
            return "None"
        return statement

speak("Hello i am your Voice Assistant")
wishMe()


if __name__ == "__main__":

    while True:
        speak("Tell me how can I help you ?")
        statement = takeCommand().lower()
        if statement==0:
            continue

        if "good bye" in statement or "bye" in statement or "stop" in statement:
            speak('your personal assistant is shutting down,Good bye')
            print('your personal assistant is shutting down,Good bye')

        if "hello" in statement:
            speak("Hello sir")
            print("Hello sir")

        if "how are you" in statement:
            speak("I am fine, Thank you for asking")
            print("I am fine, Thank you for asking")
            speak("what about you")
            statement = takeCommand()
            speak("Nice to hear that ")

        if 'who' in statement or 'know about' in statement :
            speak('Searching Wikipedia...')
            statement = statement.replace('who is', "")
            results = wikipedia.summary(statement, 1)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            time.sleep(5)
            break

        elif 'what' in statement or 'which' in statement or 'why' in statement or 'information' in statement :
            speak('Searching ...')
            statement = statement.replace('what is', "")
            results = wikipedia.summary(statement, 1)
            speak("This is something i got ")
            print(results)
            speak(results)
            time.sleep(5)
            break

        elif "recycle bin" in statement:
            winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=False)
            speak("recycle bin is emptied")

        elif "music" in statement or "song" in statement:
            speak("Here you go with music")
            music_dir = r'G:\Music'
            songs = os.listdir(music_dir)
            d = random.choice(songs)
            random = os.path.join(music_dir, d)
            playsound(random)
            break

        elif 'youtube' in statement:
            ind = statement.split().index("youtube")
            search = statement.split()[ind + 1:]
            webbrowser.open_new_tab("http://www.youtube.com/results?search_query=" + "+".join(search)                    )
            speak("Opening" + str(search) + "on youtube")
            break

        elif 'google' in statement or 'browser' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google chrome is open now")
            time.sleep(5)

        elif 'gmail' in statement or 'mail' in statement:
            webbrowser.open_new_tab("https://mail.google.com/mail/u/0/#inbox")
            speak("Google Mail open now")
            time.sleep(5)

        elif 'whatsapp' in statement or 'message' in statement:
            webbrowser.open_new_tab("https://web.whatsapp.com/")
            speak("Opening whatsapp...")
            time.sleep(5)

        elif "weather" in statement:
            api_key="8ef61edcf1c576d65d836254e11ea420"
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            speak("whats the city name")
            city_name=takeCommand()
            complete_url=base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x=response.json()
            if x["cod"]!="404":
                y=x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))
            else:
                speak(" City Not Found ")

        elif 'time' in statement:
            #strTime=datetime.datetime.now().strftime("%H:%M:%S")
            strTime=datetime.datetime.now().strftime("%I:%M %p")
            speak(f"the time is {strTime}")

        elif 'tell' in statement or 'say' in statement:
            speak('I am with python version 3.6 your persoanl assistant. I am programmed to minor tasks like'
                  'opening youtube,google chrome,gmail and play music ,predict time,search wikipedia,predict weather' 
                  'in different cities , get top headline news from times of india and you can ask me computational or geographical questions,'
                  'Open Microsoft Office like word,excel and powerpoint,tell you a joke,show the location in the map which ever city you say,'
                  'i can sign out your system, and Empty your recycle bin too!')

        elif 'news' in statement:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India,Happy reading')
            time.sleep(6)

        elif 'search'  in statement:
            statement = statement.replace("search", "")
            webbrowser.open_new_tab(statement)
            time.sleep(5)

        elif 'ask' in statement:
            speak('I can answer to computational and geographical questions and what question do you want to ask now')
            question=takeCommand()
            app_id="R2K75H-7ELALHR35X"
            client = wolframalpha.Client('R2K75H-7ELALHR35X')
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)
            break

        elif 'word' in statement:
            speak('Opening Ms word...')
            print('Opening Ms word...')
            os.startfile(r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2016\Word 2016.lnk")
            break

        elif 'powerpoint' in statement:
            speak('Opening Ms Powerpoint...')
            print('Opening Ms Powerpoint...')
            os.startfile( r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2016\PowerPoint 2016.lnk")
            break

        elif 'excel' in statement:
            speak('Opening Ms Excel...')
            print('Opening Ms Excel...')
            os.startfile(r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2016\Excel 2016.lnk")
            break

        elif "note" in statement or "remember" in statement:
            speak("What would you like me to write down?")
            note_text = takeCommand()
            note(note_text)
            speak("I have made a note of that")
            break

        elif "calculate" in statement:
            app_id = "AYAXYL-2327WP3PKJ"
            client = wolframalpha.Client(app_id)
            ind = statement.lower().split().index("calculate")
            statement = statement.split()[ind + 1:]
            response = client.query("".join(statement))
            answer = next(response.results).text
            speak("The answer" + answer)
            break

        elif "where is" in statement or "map" in statement:
            ind = statement.lower().split().index("is")
            location = statement.split()[ind + 1:]
            url = "https://www.google.com/maps/place/" + "".join(location)
            speak("This is where " + str(location) + " is.")
            webbrowser.open(url)
            break

        elif  "sign out" in statement or "bye" in statement:
            speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])

        elif"don't listen" in statement or "stop listening" in statement or "do not listen" in statement:
            speak("for how many seconds do you want me to sleep")
            a = int(takeCommand())
            time.sleep(a)
            speak(str(a) + "seconds completed. Now you can ask me anything")
        elif "exit" in statement or "quit" in statement:
            exit()

        elif 'joke' in statement:
            speak(pyjokes.get_joke())
        else:
            speak('Please say the command again.')
            time.sleep(3)

