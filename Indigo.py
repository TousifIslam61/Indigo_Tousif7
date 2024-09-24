import webbrowser
import pyttsx3
import speech_recognition as sr
import os
import time
import requests
import string
import random
from datetime import datetime
from tqdm import tqdm


recognizer = sr.Recognizer()   
engine = pyttsx3.init()



url="https://www.google.com/"
url1="https://www.youtube.com/"
url2="https://www.facebook.com/"
url3="https://www.instagram.com/"
url4="https://chatgpt.com/"
url5="https://www.pw.live/"

        
def speak_for_alarm():
    speak(f"its the time......{current_time}")

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen_command():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio).lower()
            print(f"Command received: {command}")
            return command
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return None
        except sr.RequestError:
            print("Sorry, there was a problem with the speech recognition service.")
            return None
def greet_time():
    current_hour=datetime.now().hour
    if 0<=current_hour<12:
        speak("good morning boss....what can I do for you?")
    elif current_hour>12 and current_hour<=14:
        speak("good afternoon boss....what can I do for you?")
    elif current_hour>15 and current_hour<=18:
        speak("good evening boss....what can I do for you?")
    elif current_hour>18:
        speak("good Night boss....what can I do for you?")
        

       
speak("initializing indigo...")

total=100
print("   initializing...")
for i in tqdm(range(total)):
	time.sleep(0.05)

speak("initialization sucessful....")
time.sleep(1.5)
greet_time()
command=listen_command()    

if "open google" in command:
    speak("opening google...................")
    webbrowser.open(url)
elif "open youtube" in command:
    speak("opening youtube..................")
    webbrowser.open(url1)
elif "open facebook" in command:
    speak("opening facebook....................")
    webbrowser.open(url2)
elif "open instagram" in command:
    speak("opening instagram.................")
    webbrowser.open(url3)
elif "open chat gpt" in command:
    speak("opening chat gpt.................")
    webbrowser.open(url4)
elif "open pw" in command:
    speak("opening physics wallah...................")
    webbrowser.open(url5)
elif "play music" in command:
    speak("playing Musics")
    webbrowser.open("https://www.youtube.com/watch?v=cNGjD0VG4R8")
elif "open notepad" in command:
    speak("opening notepad")
    os.system("notepad.exe")
elif "open calculator" in command:
        speak("Opening Calculator...")
        os.system("calc.exe")
elif "shut down the system" in command:
    speak("shutting down the computer")
    os.system("shutdown /s /t 1")
elif "restart the system" in command:
    speak("restarting down the computer")
    os.system("restart /r /t 1")
elif "set alarm" in command:
    speak("enter the time for the alarm to ring")
    alarm_time=input("enter the time for the alarm to ring: (HH:MM): ")
    speak("the alarm is set")

    while True:
        current_time=time.strftime("%H:%M")
        if current_time == alarm_time:
            print(f"its the time......{current_time}")
            speak_for_alarm()
            speak_for_alarm()
            speak_for_alarm()
            break
elif "weather information" in command:
    speak("enter your city name")
    city=input("enter your city name")
    
    
    url=f"https://wttr.in/{city}?format%t%20%w"

    def get_weather(city):
        response=requests.get(url)
        try:
            speak(f"the weather information for your city{city}is:")
            print(f"the weather of {city} is:{response.text}")
        except:
            print("I couldn't find")

    get_weather(city)
elif "generate password" in command:

    s1=list(string.ascii_uppercase)
    s2=list(string.ascii_lowercase)
    
    speak("Enter the lenght of the password")
    user_input=input("Enter the lenght of the password:")

    while True:
        char=int(user_input)
        try:
            if char<8:
                speak("The lenght of the password is small...try another")
                print("The lenght of the password is small…try another")
                speak("Enter another lenght of password")
                user_input=input("Enter another lenght of the password")
            else:
                break
            
        except:
            speak("only integers allowed..")
            print("only integers allowed..")
            speak("Enter another lenght of password")
            user_input=input("Enter another lenght of the password")
    random.shuffle(s1)
    random.shuffle(s2)

    p1=round(char*(69/100))
    p2=round(char*(41/100))

    result=[]

    for x in range(p1):
        result.append(s1[x])
    for x in range(p2):
        result.append(s2[x])

    random.shuffle(result)

    password="".join(result)
    speak(f"Your password is:{password}")
    print(f"Your password is:{password}")
else:
    speak("I didn't understand that. Searching the web for you...")
    search_query = command
    search_url = f"https://www.google.com/search?q={search_query}"
    webbrowser.open(search_url)
