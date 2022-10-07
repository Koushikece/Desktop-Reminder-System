import os #To manage the CSV file exists
import time #To show the notification after a particular time 
import pandas as pd #To access the CSV file columns and rows
import pyttsx3 #To use the text to speech facility for speaking text
from plyer import notification #Show text and title as notification

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

def notifyme(title, text):
    notification.notify(
        title=title,
        message=text,
        app_icon = None,
        timeout=12
    )

def textToSpeech(txt):
    engine.say(txt)
    engine.runAndWait()
    
def add_to_csv(title, text, time):
    with open("remind-data.csv", "a") as f:
        f.write(f"{title},{text},{time}\n")

def reminder():
    df = pd.read_csv("remind-data.csv")
    print("\t\t\tThe Program is running.")
    print("\t\t\t(CTRL + C) to exit")
    for index, item in df.iterrows():
        time.sleep(int(item["Time"]))
        notifyme(item["Title"], item["Message"])
        textToSpeech(item["Message"])
            
if os.path.exists("remind-data.csv"):
    with open("remind-data.csv") as f:
        content = f.read()
else:
    with open("remind-data.csv", "a") as f:
       f.write("Title,Message,Time\n")
    while True:
        title = input(" * Enter the remind short title (q to quit): ")
        if title == "q":
            break
        text = input(" * Enter the message to display : ")
        time = int(input(" * Provide time in minutes : "))
        add_to_csv(title, text, (time*60))
reminder()
        