import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib
import sys
import pyjokes

engine = pyttsx3.init('sapi5')
voices =engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voices',voices[len(voices) - 1].id)

#text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()
#to convert voice into text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listnenning.....")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=5,phrase_time_limit=8)

def sendEmail(to,content):
     server = smtplib.SMTP('smtp.gmail.com',587)
     server.ehlo()
     server.starttls()
     server.login('your email id','your password')
     server.sendmail('your email id',to,content)
     server.close()

     #to wish
def wish():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak("good morning")
    elif hour>12 and hour<18:
        speak("good afternoon")
    else:
        speak("good evening")
    speak("i am jarvis sir,please tell me how can i help you")
        


    try:
            print("Recognizing....")
            query = r.recognize_google(audio,language='en-in')
            print(f"user said: {query}")

    except Exception as e:
            speak("say that again please....")
            return "none"
    return query


    if __name__ == "__main__":
        wish()
        while True:
        # if 1:

         query = takecommand().lower()

        #logic building for task

        if "open notepad" in query:
             npath ="C:\Windows\notepad.exe"
             os.startfile(npath)

        elif "close notepad" in query:
             speak("okay sir,closing notepad")
             os.system("taskkill /f /im notepad.exe")
        
        elif "open command prompt" in query:
             os.system("start cmd")

        elif "open camera" in query:
             cap = cv2.VideoCapture(0)
             while True:
                  ret,img = cap.read()
                  cv2.imshow('webcam',img)
                  k = cv2.waitkey(50)
                  if k==27:
                       break;
             cap.release()
             cv2.destroyAllWindows()

        elif "ip address" in query:
             ip = get('https://api.ipify.org').text
             speak(f"your ip address is {ip}")

        elif "tell me a joke" in query:
             joke = pyjokes.get_joke()
             speak(joke)

        elif "shut down the system" in query:
             os.system("shutdown /s /t 5")
        
        elif "restart the system" in query:
             os.system("shutdown /r /t 5")

        

        elif "wikipedia" in query:
             speak("searching wikipedia.....")
             query = query.replace("wikipedia","")
             results = wikipedia.summary(query,sentences=2)
             speak("according to wikipedia")
             speak(results)
             #print(results)
        
        elif "open youtube" in query:
             webbrowser.open("youtube.com")

        elif "close youtube" in query:
             speak("okay sir,closing youtube")
        
        elif "open facebook" in query:
             webbrowser.open("facebook.com")

        elif "open google" in query:
             speak("sir,what should i search on google")
             cm = takecommand().lower()
             webbrowser.open(f"{cm}")
        
        elif "send message" in query:
             kit.sendwhatmsg("+919173717346","this is testing protocol",2,25)

        elif "play song on youtube" in query:
             kit.playonyt("see you again")
        
        elif "email to harsh" in query:
            try:
                 speak("what should i say?")
                 content = takecommand().lower()
                 to = "harshjogadiya001@gmail.com"
                 sendEmail(to,content)
                 speak("Email has been sent to harsh")

            except Exception as e:
                 print(e)
                 speak("sorry sir,i am not able to sent this mail to harsh")

        elif "you can sleep" in query:
             speak("thanks for using me sir,have a good day")
             sys.exit()


        speak("sir,dp you have any other work")

                  




                     
