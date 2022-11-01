from tkinter import *
import speech_recognition as sr
import pyttsx3
from datetime import datetime

import webbrowser
import subprocess

root = Tk()
root.geometry("500x500")
root.title("Speech Recognition")
root.configure(bg="cornflower blue")

label1 = Label(root,text="Welcome to your persnol desktop assistant",bg="cornflower blue",font=("Arial",15,"bold"))
label1.place(relx=0.5,rely=0.2,anchor=CENTER)

text_to_speech = pyttsx3.init()

def speak(audio):
    text_to_speech.say(audio)
    text_to_speech.runAndWait()

def r_audio():
    speak("How can i help you")
    speech_recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        audio = speech_recognizer.listen(source)
        voice_data = ""
        try:
            voice_data = speech_recognizer.recognize_google(audio,language="en-in")
        except sr.UnknownValueError:
            print("Please repeat i did not get that")
            speak("Please repeat i did not get that")
            r_audio()
    print(voice_data)
    
    respond(voice_data)
    
def respond(voice_data):
    lower = voice_data.lower()
    
    if "name" in lower:
        print("My name is Ethihas")
        speak("My name is Ethihas")
    if "time" in lower:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print(current_time)
        speak(current_time)
    if "search" in lower:
        print("Opening Google")
        speak("Opening Google")
        webbrowser.get().open("https://www.google.com/")
    if "videos" in lower:
        print("Opening youtube")
        speak("Opening youtube")
        webbrowser.get().open("https://www.youtube.com/")
    if "editor" in lower:
        print("Opening notepad")
        speak("Opening notepad")
        subprocess.Popen(["notepad.exe"])
    
btn = Button(root,text="Start",bg="orange",fg="cyan",command=r_audio(),padx=10,pady=1,font=("Arial",11,"bold"),relif=FLAT)
btn.place(relx=0.5,rely=0.7,anchor=CENTER)
root.mainloop()