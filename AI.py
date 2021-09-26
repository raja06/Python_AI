import speech_recognition as sr      #import required modules
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
import cv2
import wolframalpha
import json
import requests
import pyaudio
import tkinter
import random
import operator
import winshell
import pyjokes
import feedparser
import smtplib
import ctypes
import shutil
from youtubesearchpython import *
from twilio.rest import Client
from clint.textui import progress
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen
from PIL import Image

# Setting up the speech engine
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)   #voice id can be set as 0 or 1, 0-male voice, 1-female voice

# run and wait function
def speak(text):
    engine.say(text)
    engine.runAndWait()

# initiate a function to greet the user
def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Hello,Good Morning")
        print("Hello,Good Morning")
    elif hour>=12 and hour<18:
        speak("Hello,Good Afternoon")
        print("Hello,Good Afternoon")
    else:
        speak("Hello,Good Evening")
        print("Hello,Good Evening")
    global assname
    assname = ("Raja")
    speak("I am your Assistant")
    speak(assname)

# set user name
def usrname():
    speak("what should i call you?")
    uname=takeCommand()
    speak("Welcome")
    speak(uname)
    columns=shutil.get_terminal_size().columns
    print("#####################")
    print("Welcome", uname)
    print("#####################")

    speak("How can i Help you")
    print("How can i help you?")
    
# Setting up the command function for AI assistant
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)

        try:
            statement=r.recognize_google(audio, language='en-in')
            print(f"user said:{statement}\n")

        except Exception as e:
            speak("Pardon me, please say that again")
            return "None"
        return statement

speak("Loading your AI personal assistant Raja")
print('Loading your AI personal assistant Raja')

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()

    #Enable low security in gmail
    server.login('example@gmail.com', '**Password**')
    server.sendmail('example@gmail.com', to, content)
    server.close()
    
# The main function
if __name__=='__main__':
    clear = lambda: os.system('cls')
    #This function will clean any command before execution of this python file
    clear()
    wishMe()
    usrname()
    while True:
        statement = takeCommand().lower()
        if statement==0:
            continue

        if "good bye" in statement or "ok bye" in statement or "stop" in statement:
            speak('your personal assistant Raja is shutting down,Good bye')
            print('your personal assistant Raja is shutting down,Good bye')
            break
            
        # Fetching data from wikipedia
        if 'in wikipedia' in statement:
            speak('Searching Wikipedia...')
            statement =statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            
        # Accessing the web browser-google, g-mail and youtube
        elif 'youtube' in statement:
            speak("searching youtube video")
            statement=statement.replace("youtube", "")
            autosearch = CustomSearch(statement, VideoUploadDateFilter.lastHour, limit=2)
            for i in range(2):
                Result=autosearch.result()['result'][i]['link']
            webbrowser.open_new_tab(Result)
            time.sleep(5)

        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google chrome is opening")
            time.sleep(5)

        elif 'open gmail' in statement:
            webbrowser.open_new_tab("https://www.gmail.com")
            speak("Google Mail opening")
            time.sleep(5)

        elif 'open stakoverflow' in statement:
            webbrowser.open_new_tab("https://stackoverflow.com/login")
            speak("here is stackoverflow")
            
        # Accessing music
        elif 'play music' in statement or 'play song' in statement:
            speak("Here you go with music")
            music_dir = r"E:\songs"
            songs = os.listdir(music_dir)
            print(songs)
            d = random.choice(songs)
            random = os.startfile(os.path.join(music_dir, d))
            
        # Sending gmail
        elif 'send mail' in statement:
            try:
                speak("What should i say?")
                content = takeCommand()
                speak("Whome should i send")
                to = input("Enter To address:")
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("I am not able to send this email")
                
            # change user name
            elif "change my name to" in statement:
                statement=statement.replace("change my name to", "")
                assname = statement
                
            # for wish
            elif 'how are you' in statement:
                speak("I am fine, Thank you")
                speak("How are you")

            elif 'fine' in statement or 'good' in statement:
                speak("It's good to know that you are fine")

            elif "what's your name" in statement or 'what is your name' in statement:
                speak("my friends call me")
                speak(assname)
                print("My friends call me", assname)
                
            # jokes statement
            elif 'joke' in statement:
                speak(pyjokes.get_joke())
                
            # calculator wedget
            elif "calculate" in statement:
                app_id = "APP_ID"
                client = wolframalpha.Client(app_id)
                indx = statement.lower().split().index('calculate')
                statement = statement.split()[indx + 1:]
                res = client.query(''.join(statement))
                answer = (next(res.results).plaintext)
                print("The answer is " + answer)
                speak("The answer is " + answer)
                
           # Predicting time
           elif 'time' in statement:
              strTime=datetime.datetime.now().strftime("%H:%M:%S")
              speak(f"the time is {strTime}")
              
           # To fetch latest news
           elif 'latest news' in statement:
              try:
                  r=requests.get("https://timesofindia.indiatimes.com/news")
                  c=r.content
                  soup=BeautifulSoup(c,"html.parser")
                  all=soup.find_all("div",{"class":"main-content"})
                  speak("Here are some top news from Times of India")
                  print('''==============TIMES OF INDIA================'''+ '\n')
                  i=0
                  while True:
                      for item in all:
                          if i < 4:
                              i=i+1
                              news=item.find_all("li")[0+i].text
                              print(news)
                              speak(news)
                          else:
                              continue
                      break
              except Exception as e:
                  print(str(e))
                  
           # Capturing photo
           elif "open camera" in statement or "take a photo" in statement or "Take a pic" in statement:
              camera = cv2.VideoCapture(0)   #0-default cam, 1-external cam
              time.sleep(0.1)  # If you don't wait, the image will be dark
              return_value, image = camera.read()
              cv2.imwrite("img.jpg", image)
              del(camera)  # so that others can use the camera as soon as possible
           
           elif 'show photo' in statement or 'show me that pic' in statement:
              img=cv2.imread("img.jpg", 1)
              cv2.imshow("Rose Image",img)
              cv2.waitKey(2000)
              
           elif 'delete that pic' in statement or 'delete that photo' in statement:
              list = os.listdir(r"//dir//")
              for file in list:
                  if file.endswith('.jpg'):
                      os.remove(file)
                      
           # Searching data from web
           elif 'search' in statement:
              speak('searching for answer')
              statement=statement.replace("search", "")
              results = wikipedia.summary(statement, sentences=3)
              speak('According to Google')
              print(results)
              speak(results)
              
           # Setting up AI assistant to answer geographical and computational questions
           elif 'ask' in statement:
              speak('I can answer to computational and geographical questions and what question do you want to ask now')
              question=takeCommand()
              app_id="APP_ID"
              client=wolframalpha.Client(app_id)
              res=client.query(question)
              answer=next(res.results).text
              speak(answer)
              print(answer)
              
           # Extra features
           elif 'who are you' in statement or 'what can you do' in statement:
              speak('I am Raja your personal assistant. I am programmed to do minor tasks like'
              'opening youtube, google, gmail and stackoverflow, predict time, take a photo, search wikipedia, predict weather'
              'In different cities, get top headline news from times of india and you can ask me computational or geographical questions too!')

           elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
              speak("I was built by Raja")
              print("I was built by Raja")
              
           # To forecast weather
           elif "weather" in statement:
              api_key = "API_KEY"
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
                
           # for humor
           elif "who i am" in statement:
              speak("If you talk then definately you are human.")

           elif "why you came to world" in statement:
              speak("Thanks to Raja. further It's a secret")

           elif "is love" in statement:
              speak("It is 7th sense that distroy all other senses")
              
           elif "change your name" in statement:
              speak("Sorry i already have a name and my name name is Raja")
              print(Sorry i already have a name and my name is Raja")
           
           elif "Good Morning" in statement:
              speak("A warm" + statement)
              speak("How are you")
              speak(assname)
              
           elif "how are you" in statement:
              speak("I am fine, glad you ask me that")
           
           # search command
           elif "what is" in statement or "who is" in statement:
              client = wolframalpha.Client("RE6G7H-5YYH5YYRL9")
              res = client.query(statement)
              try:
                  print(next(res.results).text)
                  speak(next(res.results).text)
              except StopIteration:
                  print("No results")
           
           # lock window
           elif 'lock window' in statement:
              speak("Locking this device")
              ctypes.windll.user32.LockWorkStation()

           elif 'shutdown system' in statement or 'Turn off system' in statement:
              speak("Hold on a seconds! your system is on it's way to shutdown")
              subprocess.call('shutdown / p / f')

           elif 'empty recycle bin' in statement:
              winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
              speak("Recycle Bin Recycled")

           elif "don't listen" in statement or "stop listening" in statement:
              speak("For how much time you want to stop", + assname, + "from listening commands")
              a = int(takeCommand())
              time.sleep(a)
              print(a)

           elif "where is" in statement:
              statement=statement.replace("where is", "")
              location=statement
              speak("User asked to Locate")
              speak(location)
              webbrowser.open_new_tab("https://www.google.n1/maps/place/" + location + "")
              
           # Restare commands
           elif "restart" in statement:
              subprocess.call(["shutdown", "/r"])

           elif "hibernate" in statement or "sleep" in statement:
              speak("Hibernating")
              subprocess.call("shutdown/h")
              
           # write a note command
           elif "write a note" in statement:
              speak("What should i write")
              note=takeCommand()
              file=open('new.txt', 'w')
              speak("Should i include date and time")
              snfm = takeCommand()
              if 'yes' in snfm or 'sure' in snfm:
                  strTime=datetime.datetime.now().strftime("%H:%M:%S")
                  file.write(strTime)
                  file.write(" :- ")
                  file.write(note)
              elif 'no' in snfm or 'nope' in snfm:
                  file.write(note)

           elif "show note" in statement:
              speak("Showing Notes")
              file=open("new.txt", 'r')
              print(file.read())
              speak(file.read(6))

           elif "Raja" in statement:
              wishMe()
              speak("Rose 1 point o in your service")
              speak(assname)
              
           # To log-off your pc
           elif "log off" in statement or "sign out" in statement:
              speak("Ok, your pc will log off in 10 sec make sure you exit from all applications")
              subprocess.call(["shutdown", "/1"])
              
           #send a message command
           elif "send message" in statement:
              # need to create an account on Twilio to use this service
              account_sid = 'ACCOUNT_SID'
              auth_token = 'AUTH_TOKEN'
              client = Client(account_sid, auth_token)
              message = client.messages \
                                      .create(body = takeCommand(),
                                      from_= '+91**********',
                                      to = takeCommand())
            print(message.sid)
            
time.sleep(3)
