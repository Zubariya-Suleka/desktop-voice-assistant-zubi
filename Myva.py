import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser as wb
import os
import pywhatkit

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def time():
    times = datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is")
    speak(times)
    print("The current time is ", times)


def date():
    day = int(datetime.datetime.now().day)
    month = int(datetime.datetime.now().month)
    year = int(datetime.datetime.now().year)
    speak("the current date is")
    speak(day)
    speak(month)
    speak(year)
    print("The current date is " + str(day) + "/" + str(month) + "/" + str(year))


def greeting():
    print("Welcome back")
    speak("Welcome back")

    hour = datetime.datetime.now().hour
    if 4 <= hour < 12:
        speak("Good Morning Sir!!")
        print("Good Morning Sir!!")
    elif 12 <= hour < 16:
        speak("Good Afternoon Sir!!")
        print("Good Afternoon Sir!!")
    elif 16 <= hour < 24:
        speak("Good Evening Sir!!")
        print("Good Evening Sir!!")
    else:
        speak("Good Night Sir, See You Tomorrow")

    speak("I am Zubi, your virtual assistant, please tell me how may I help you.")
    print("I am Zubi, your virtual assistant, please tell me how may I help you.")


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(query)

    except Exception as e:
        print(e)
        speak("Please say that again")
        return "Try Again"

    return query


if __name__ == "__main__":
    greeting()
    while True:
        query = takecommand().lower()
        if "time" in query:
            time()

        elif "date" in query:
            date()

        elif "who are you" in query:
            speak("I'm ZUBI and I'm a virtual desktop voice assistant.")
            print("I'm ZUBI and I'm a virtual desktop voice assistant.")

        elif "how are you" in query:
            speak("I'm fine sir, What about you?")
            print("I'm fine sir, What about you?")

        elif "fine" in query:
            speak("Glad to hear that sir!!")
            print("Glad to hear that sir!!")

        elif "good" in query:
            speak("Glad to hear that sir!!")
            print("Glad to hear that sir!!")

        elif "open youtube" in query:
            speak("Opening Youtube")
            wb.open("youtube.com")

        elif "open google" in query:
            speak("Opening google")
            wb.open("google.com")

        elif "google search" in query or "search on web" in query:
            try:
                speak("What should I search?")
                print("What should I search?")
                search = takecommand()
                searchurl = '+'.join(search.split())
                url = 'http://www.google.com/search?q='+searchurl
                wb.open_new_tab(url)
                speak("here is what I found for" + search)
                print(search)

            except Exception as e:
                speak("Can't open now, please try again later.")
                print("Can't open now, please try again later.")

        elif "find location" in query:
            try:
                speak("What should I search?")
                print("What should I search?")
                location = takecommand()
                url='http://www.google.nl/maps/place/'+location
                wb.open_new_tab(url)
                speak("Here is the location of "+location)
                print(location)

            except Exception as e:
                speak("Can't find the location now, please try again later.")
                print("Can't find the location now, please try again later.")

        elif "youtube search" in query or "play youtube video" in query:
            try:
                speak("What should I play?")
                print("What should I play?")
                v_search = takecommand()
                speak("playing your video now")
                pywhatkit.playonyt(v_search)
                print(v_search)

            except Exception as e:
                speak("Can't play the video now, please try again later.")
                print("Can't play the video now, please try again later.")

        elif "remember that" in query:
            speak("What should I remember")
            data = takecommand()
            speak("You told me to remember that" + data)
            print("You told me to remember that " + str(data))
            remember = open(".venv/data.txt", "w")
            remember.write(data)
            remember.close()

        elif "do you remember anything" in query:
            remember = open(".venv/data.txt", "r")
            speak("You told me to remember that" + remember.read())
            print("You told me to remember that " + str(remember))

        elif 'open notepad' in query:
            speak('Okay! Opening Notepad')
            os.system('notepad')

        elif 'close notepad' in query:
            speak('Okay! Closing Notepad')
            os.system('taskkill /F /IM notepad.exe')

        elif 'open command prompt' in query:
            speak('Okay! Opening Command Prompt')
            os.system('start cmd')

        elif 'close command prompt' in query:
            speak('Okay! Closing Command Prompt')
            os.system('taskkill /F /IM cmd.exe')

        elif 'close chrome' in query:
            speak('Okay! Closing Chrome')
            os.system('taskkill /F /IM chrome.exe')

        elif "shutdown" in query:
            speak("shutting down")
            os.system('shutdown -s')

        elif "offline" in query:
            speak("Goodbye. Hope you had good assistance")
            quit()
