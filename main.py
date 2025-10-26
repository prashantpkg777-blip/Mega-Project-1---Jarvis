import speech_recognition as sr
import pyttsx3
import webbrowser
import requests
import os
import time

engine = pyttsx3.init()
r = sr.Recognizer()

def speak(text):
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()

def listen(timeout=None, phrase_time_limit=None):
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        print("Listening...")
        audio = r.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
    try:
        return r.recognize_google(audio).lower()
    except:
        return ""

def process_command(command):
    if "google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")
    elif "youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
    elif "facebook" in command:
        speak("Opening Facebook")
        webbrowser.open("https://www.facebook.com")
    elif "news" in command:
        speak("Fetching the latest news...")
        try:
            url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey=40e9619e9c71486da75e3ee49840b059"
            response = requests.get(url)
            articles = response.json().get("articles", [])[:5]
            for i, article in enumerate(articles):
                speak(f"News {i+1}: {article['title']}")
        except Exception as e:
            speak("Sorry, cannot fetch news now.")
            print(e)
    elif "exit" in command:
        speak("Goodbye!")
        exit()
    else:
        speak("I didn't understand that command.")

# main loop 
speak("Jarvis is online.")
while True:
    print("Waiting for wake word...")
    wake = listen(timeout=5, phrase_time_limit=5)
    if "jarvis" in wake:
        speak("Yes bro")
        command = listen(timeout=10, phrase_time_limit=7)
        if command:
            process_command(command)
        else:
            speak("I didn't catch that.")
