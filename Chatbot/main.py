import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import pywhatkit

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Ohayo Gozaimasu. Good Morning")
    elif hour>=12 and hour<18:
        speak("Konnichiwa. Good Afternoon")
    else:
        speak("Konbamwa.. Good Evening")             

    speak("I am Mai-San, your personal AI assistant. Please Tell Me How May I Help you ?")    

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')   
        print("User Said =" + str(query) + "\n") 

    except Exception as e:

        print("Say That Again Please...")
        return "None"
    
    return query

if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak("Searching Wikipedia")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 2)
            speak("According to wikipedia")
            speak(results)
            break

        elif 'open youtube' in query:
            speak("Opening Youtube")
            webbrowser.open("youtube.com")
            break

        elif 'open google' in query:
            webbrowser.open("google.com")



      

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Current time is {strTime}")
            
        elif 'play' in query:
            song = query.replace("play","")
            speak("Playing the requested song")
            pywhatkit.playonyt(song)

        elif 'shutdown' in query:
            speak("Have A Good Day")
            break    
            









