import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import pyaudio
import subprocess
import pywhatkit as wk



MASTER = "sir"

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

#speak fun to pronounce the given string
def speak(text):
    engine.say(text)
    engine.runAndWait()

#the hello fun
def wishme():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour <12:
        speak("Good Morning "+ MASTER)
    elif hour>=12 and hour <18:
        speak("Good Afternoon "+ MASTER)
    else:
        speak("Good Evening "+ MASTER)


def takecmd():
    r=sr.Recognizer()
    with sr.Microphone() as source :
        print("Listening...")
        audio  = r.listen(source)
    try :
        print("recognizing...")
        query = r.recognize_google(audio,language='en-us')
        #print(f"user said :{query}\n")

    except Exception as e:
        # speak("Say That again !")
        query = "None"
    return query

speak("Initializing ...")
wishme()
speak(f"{MASTER} What do you want me to do for you : ")


def assistant(query):


    if 'time' in query:
        time = datetime.datetime.now().strftime("%H:%M")
        speak(f"The current Time is {time}")


    elif "wikipedia" in query :
        query = query.replace('wikipedia','')
        speak("Searching Wikipedia ...")
        results = wikipedia.summary(query,sentences=2)
        speak(results)

        speak("Done Sir, Anything Else !")
        
    elif 'search on youtube' in query:
            query = query.replace("search on youtube", "")
            webbrowser.open(f"Www.youtube.com/results?search_query={query}")
            wk.playonyt(f"{qrry}")
                

    elif "open" in query :
        try :
            website = query.split(' ')
            webbrowser.open("https://"+website[website.index("open")+1]+".com")
            speak(website[website.index("open")+1] + "is Opened ")
        except Exception as e :
            speak("i can't see it")


    elif "bye" in query :
        speak(f"My pleasure to help you {MASTER}, See you later")
        return 0


    # else:
    # speak("I am not able to do this !")


while True:
    if assistant(takecmd().lower())==0:
      break

