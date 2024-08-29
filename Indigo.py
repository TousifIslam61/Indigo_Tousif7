import webbrowser
import pyttsx3
import speech_recognition as sr
import google.generativeai as genai
import os


recognizer = sr.Recognizer()   
engine = pyttsx3.init()




url="https://www.google.com/"
url1="https://www.youtube.com/"
url2="https://www.facebook.com/"
url3="https://www.instagram.com/"
url4="https://chatgpt.com/"
url5="https://www.pw.live/"

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
        
speak("initializing indigo.....")
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
elif "shut down" in command:
    speak("shutting down the computer")
    os.system("shutdown /s /t 1")
elif "restart" in command:
    speak("restarting down the computer")
    os.system("restart /r /t 1")
else:
    speak("I didn't understand that. Searching the web for you...")
    search_query = command  # Use the command as the search query
    search_url = f"https://www.google.com/search?q={search_query}"
    webbrowser.open(search_url)