import pyttsx3
import datetime
import speech_recognition as sr #pip install speacheRcogination
import wikipedia
import webbrowser
import os
import smtplib
#import pyaudio
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice',voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def sendemail(to,content):
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login("mygmai.com","my password")
    server.sendmail("mygmail.com",to,content)
    server.close()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning!")
    elif hour>=12 and hour<18:
        speak("good afternoon!")
    else:
        speak("good evening!")
    speak("i am magic peach")
    speak("your  friend")
    speak("please tell me how can i help you ")

def takecommand():
    #it take microphone input from the user

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening......")
        r.pause_threshold =1
        audio=r.listen(source)

    try:
       query=r.recognize_google(audio,language='en-in')
       print(f"user said:{query}\n")

    except Exception as e:
        print(e)

        print("say it again please...")
        return "none"
    return query



if __name__=="__main__":
    wishme()
    #speak("shivam is a good boy")
    while True:
        quary= takecommand().lower()

        # logic for executing tastk
        if "tell me " in quary:
            speak("searching for you.....")
            quary=quary.replace("tell me","")
            results=wikipedia.summary(quary,sentences=2)
            speak("according to wikipedia")
            print(results)
            speak(results)
         # to open youtube
        elif 'open youtube' in quary:
            webbrowser.open('youtube.com')
            # to open google
        elif 'open google' in quary:
            webbrowser.open('google.com')
            #open your whatsapp
        elif 'open whatsapp' in quary:
            webbrowser.open("whatsapp")
            #to play music
        elif 'play music' in quary:
            music_dir="  "
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
            # to knoe the present time
        elif 'the time' in quary:
            strtime=datetime.datetime.now().strftime("%H:%M:%s")
            speak(f"sir, the time is {strtime} ")
        #to open any app from your desktop
        elif 'open code' in quary:
            codepath=" put your path here"
            os.startfile(codepath)
            #to send to particular person from your contact make a dictanory above then code here
        elif 'email to name' in quary:
            try:
                speak("email_content")
                content= takecommand()
                to="abc@gmail.com"
                sendemail(to,content)
                speak("email has been sent")
            except Exception as e:
                print(e)
                speak("sorry my friend unable to send email")