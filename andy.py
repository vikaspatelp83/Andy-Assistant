# andy the ai assistant
# originally coded by Vikas Patel
# at github.com/vikaspatelp83
# twitter.com/DevDp430

import wikipedia
import pyttsx3
import speech_recognition as sr
import wolframalpha
import webbrowser 
import datetime
import os
import sys
import time
import random
#from scrapimdb import ImdbSpider

# wolfram alpha client
client = wolframalpha.Client('RHVGGQ-YG74U8Q5L2')

# start voice engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices)
engine.setProperty('voice', voices[1].id)
rate = engine.getProperty('rate')   # getting details of current speaking rate
engine.setProperty('rate', 190)

# end voice engine


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning boss")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon boss")
    else:
        speak("Good Evening boss")
    speak('')
    speak("I am andy, your personal assistant, what can i do for you.")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        speak("I'm listening")
        r.pause_threshold = 0.5
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"Boss : {query}")
        except Exception as e:
            print("Andy : Say that again please.")
            speak("Say that again please.")
            return "None"
        return query

if __name__ == "__main__":
    print("Andy Initialized ...")
    
    wishme()

    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    music_dir = "C://Users//LENOVO//Music//Vik"
    video_dir = "c://Users//Lenovo//Videos"
    movie_dir = ["G://Movies//Bollywood","G://Movies//hollywood","G://Movies//tollywood"]

    # logic for executing tasks
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace('wikipedia',"")
            result = wikipedia.summary(query,sentences = 3)
            speak("According to Wikipedia")
            print(result)
            speak(result)
        elif "listen andy" in query or "listen andee" in query or "suno" in query or "are you ready" in query:
            print("Andy : Yes Boss")
            speak("Yes boss,")
        elif "hello andy" in query:
            speak("Hello Boss")
            print("Andy : Hello Boss")
        elif "what can you do for me" in query or "your job" in query:
            print("Andy : I can send emails, search websites, play music, play movies, launch applications,\
search wikipedia, search internet and many more. ")
            speak("I can send emails, search websites, play music, play movies, launch applications,\
            search wikipedia, search internet and many more. ")

        elif 'introduce' in query or 'who are you' in query:
            introduction = "Hi I'm Andy, An AI based personal assistant. My creater is Vikas Patel alias Dave , He is a developer \
and my boss, He is now improving my features by working on me, he is teaching me new things to do. Some of my features \
are , search wikipedia, open websites, play music, play videos, open applications, send emails and many more."
            print(f"Andy : {introduction}")
            speak(introduction)

        elif 'open google' in query:
            speak("opening google")
            webbrowser.get(chrome_path).open("google.com")  
    
        elif 'open youtube' in query:
            speak("opening youtube")
            webbrowser.get(chrome_path).open("youtube.com")
            
        elif 'open twitter' in query:
            speak("opening twitter")
            webbrowser.get(chrome_path).open("twitter.com")

        elif 'open facebook' in query:
            speak("opening facebook")
            webbrowser.get(chrome_path).open("facebook.com")
        
        elif 'open reddit' in query:
            speak("opening reddit")
            webbrowser.get(chrome_path).open("reddit.com")
        
        elif 'open stackoverflow' in query:
            speak("opening tensorflow")
            webbrowser.get(chrome_path).open("stackoverflow.com")
        
        elif 'open instagram' in query:
            speak("opening instagram")
            webbrowser.get(chrome_path).open("instagram.com")
        
        elif 'open w3schools' in query:
            speak("opening w3schools")
            webbrowser.get(chrome_path).open("w3schools.org")
        
        elif 'open realpython' in query or 'real python' in query:
            speak("opening realpython")
            webbrowser.get(chrome_path).open("realpython.com")
        
        elif 'open github' in query:
            speak("opening github")
            webbrowser.get(chrome_path).open("github.com")
        
        elif 'open gitpod' in query:
            speak("opening gitpod")
            webbrowser.get(chrome_path).open("gitpod.io")
        
        elif 'open tensorflow' in query:
            speak("opening tensorflow")
            webbrowser.get(chrome_path).open("tensorflow.org")
        
        elif 'open gmail' in query:
            speak("opening gmail")
            webbrowser.get(chrome_path).open("gmail.com")

        elif 'open udemy' in query:
            speak("opening udemy")
            webbrowser.get(chrome_path).open("udemy.com")
        
        elif 'open tutsgalaxy' in query:
            speak("opening tutsgalaxy")
            webbrowser.get(chrome_path).open("tutsgalaxy.com")

        elif 'open udacity' in query:
            speak("opening udacity")
            webbrowser.get(chrome_path).open("udacity.com")
        
        elif 'open hackerrank' in query:
            speak("opening hackerrank")
            webbrowser.get(chrome_path).open("hackerrank.com")
                      
        elif 'open hackerearth' in query:
            speak("opening hackerearth")
            webbrowser.get(chrome_path).open("hackerearth.com")

        elif 'open freecodecamp' in query:
            speak("opening freecodecamp")
            webbrowser.get(chrome_path).open("freecodecamp.techcrunch")

        elif 'open techcrunch' in query:
            speak("opening techcrunch")
            webbrowser.get(chrome_path).open("techcrunch.com")

        elif 'open pdfdrive' in query:
            speak("opening pdfdrive")
            webbrowser.get(chrome_path).open("pdfdrive.net")

        elif 'open whatsapp' in query:
            speak("opening whatsapp")
            webbrowser.get(chrome_path).open("web.whatsapp.com")

        elif 'open paypal' in query:
            speak("opening paypal")
            webbrowser.get(chrome_path).open("paypal.com")

        elif 'open colab' in query:
            speak("opening colab")
            webbrowser.get(chrome_path).open("colab.research.google.com")
        
        elif 'open hidden wiki' in query or 'hiddenwiki' in query:
            speak("opening hiddenwiki")
            webbrowser.open("zqktlwi4fecvo6ri.onion//wiki")

        elif 'open amazon' in query:
            speak("opening amazon")
            webbrowser.get(chrome_path).open("amazon.in")

        elif 'open flipkart' in query:
            speak("opening flipkart")
            webbrowser.get(chrome_path).open("flipkart.com")
        # play songs 
        elif 'play music' in query:
            songs = os.listdir(music_dir)
            speak("Started playing music")
            i = random.randint(0,len(songs)-1)
            os.startfile(os.path.join(music_dir,songs[i]))
        # play video
        elif 'play video' in query:
            videos = os.listdir(video_dir)
            speak("Started playing videos")
            i = random.randint(0,len(videos)-1)
            os.startfile(os.path.join(video_dir,videos[i]))
        # play movies
        elif 'play movie' in query:
            i = random.randint(0,len(movie_dir)-1)
            speak("Started playing movies")
            movies = os.listdir(movie_dir[i])
            j = random.randint(0,len(movies)-1)
            os.startfile(os.path.join(movie_dir[i],movies[j]))
        # time
        elif 'the time' in query:
            str_time = datetime.datetime.now().strftime("%H:%M:%S")
            print(str_time)
            speak(f"Boss The time is {str_time}")
        # date
        elif 'the date' in query:
            date_today = datetime.date.today()
            print(f"Andy : Boss today is {date_today.day}  {date_today.month} {date_today.year}")
            speak(f"Boss today is {date_today.day} of {date_today.month} {date_today.year}")

        elif "search" in query:
            try:
                ques = query.replace('search',"")
                # print(f"Boss: {ques}")
                print("Andy : Searching the web...")                  
                speak("Searching the web...")
                result = client.query(ques)
                output = next(result.results).text
                print(output)
                speak(output)
            except Exception as e:
                print(e)
                print("Andy : No Query specified")
                speak("No Query specified")

        # elif "tell me joke" in query:
        #     i = random.randint(0,len(joke)-1)
        #     speak(joke[i])       


        # exit 
        elif 'take rest' in query or 'quit' in query:
            print("Bye Boss, Have a nice time.")
            speak("Bye Boss, Have a nice time.")
            sys.exit()
        
        # open applications 
      


        # email
        time.sleep(1)
