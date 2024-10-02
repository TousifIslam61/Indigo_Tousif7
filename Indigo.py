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

# URLs for quick access
urls = {
    "google": "https://www.google.com/",
    "youtube": "https://www.youtube.com/",
    "facebook": "https://www.facebook.com/",
    "instagram": "https://www.instagram.com/",
    "chatgpt": "https://chatgpt.com/",
    "pw": "https://www.pw.live/"
}


def speak_for_alarm():
    speak(f"it's the time... {current_time}")


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
    current_hour = datetime.now().hour
    if 0 <= current_hour < 12:
        speak("Good morning, boss. What can I do for you?")
    elif 12 <= current_hour <= 14:
        speak("Good afternoon, boss. What can I do for you?")
    elif 15 <= current_hour <= 18:
        speak("Good evening, boss. What can I do for you?")
    else:
        speak("Good night, boss. What can I do for you?")


speak("Initializing Indigo...")


total = 100
print("   Initializing...")
for i in tqdm(range(total)):
    time.sleep(0.05)

speak("Initialization successful...")
time.sleep(1.5)
greet_time()

command = listen_command()

if command is not None:
    if "open google" in command:
        speak("Opening Google...")
        webbrowser.open(urls["google"])
    elif "open youtube" in command:
        speak("Opening YouTube...")
        webbrowser.open(urls["youtube"])
    elif "open facebook" in command:
        speak("Opening Facebook...")
        webbrowser.open(urls["facebook"])
    elif "open instagram" in command:
        speak("Opening Instagram...")
        webbrowser.open(urls["instagram"])
    elif "open chat gpt" in command:
        speak("Opening ChatGPT...")
        webbrowser.open(urls["chatgpt"])
    elif "open pw" in command:
        speak("Opening Physics Wallah...")
        webbrowser.open(urls["pw"])
    elif "play music" in command:
        speak("Playing music...")
        webbrowser.open("https://www.youtube.com/watch?v=cNGjD0VG4R8")
    elif "open notepad" in command:
        speak("Opening Notepad...")
        os.system("notepad.exe")
    elif "open calculator" in command:
        speak("Opening Calculator...")
        os.system("calc.exe")
    elif "shut down the system" in command:
        speak("Shutting down the computer...")
        os.system("shutdown /s /t 1")
    elif "restart the system" in command:
        speak("Restarting the computer...")
        os.system("shutdown /r /t 1")
    elif "set alarm" in command:
        speak("Enter the time for the alarm to ring")
        alarm_time = input("Enter the time for the alarm to ring (HH:MM): ")
        speak("The alarm is set")

        while True:
            current_time = time.strftime("%H:%M")
            if current_time == alarm_time:
                print(f"It's the time... {current_time}")
                speak_for_alarm()
                break
    elif "weather information" in command:
        speak("Enter your city name")
        city = input("Enter your city name: ")

        def get_weather(city_name):
            url = f"https://wttr.in/{city_name}?format=%t %w"
            response = requests.get(url)
            try:
                speak(f"The weather information for your city {city_name} is:")
                print(f"The weather of {city_name} is: {response.text}")
            except:
                speak("I couldn't find the weather information.")
                print("I couldn't find the weather information.")

        get_weather(city)
    elif "generate password" in command:
        s1 = list(string.ascii_uppercase)
        s2 = list(string.ascii_lowercase)
        s3 = list(string.digits)
        s4 = list(string.punctuation)

        speak("Enter the length of the password")
        while True:
            try:
                char = int(input("Enter the length of the password: "))
                if char < 8:
                    speak("The length of the password is too small. Try again.")
                    print("The length of the password is too small. Try again.")
                else:
                    break
            except ValueError:
                speak("Only integers allowed.")
                print("Only integers allowed.")

        random.shuffle(s1)
        random.shuffle(s2)
        random.shuffle(s3)
        random.shuffle(s4)

        password_chars = s1[:char // 4] + s2[:char // 4] + s3[:char // 4] + s4[:char // 4]
        random.shuffle(password_chars)

        password = "".join(password_chars[:char])
        speak(f"Your password is: {password}")
        print(f"Your password is: {password}")
    else:
        speak("I didn't understand that. Searching the web for you...")
        search_url = f"https://www.google.com/search?q={command}"
        webbrowser.open(search_url)
else:
    speak("I didn't catch any command. Please try again.")

