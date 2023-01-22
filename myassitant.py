import os
os.system("pip install pyttsx3")
os.system("pip install pypiwin32")
os.system("pip install datetime")
os.system("pip install speech_recognition")
os.system("pip install random")
os.system("pip install webbrowser")
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser


from random import choice

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
# print(voices[1].id)
engine.setProperty("voice", voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    """ this will wish user
    """
    hour = int(datetime.datetime.now().hour)
    if hour >= 4 and hour <= 12:
        speak("good morning sir ")
    elif hour >= 12 and hour <= 18:
        speak("good afternoon sir")
    elif hour >= 18 and hour <= 20:
        speak("good evening sir")
    else:
        speak("good night sir")

    speak("hello sir myself MUKESH ASSISTANT HOW CAN I HELP U?")


# def sendEmail():
#     pass
#   will not work due to change in privacy of google


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening.....\n please say how i can help u?....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recogining dear wait for  a while...........")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said :--{query}")
    except Exception as e:
        # print(e)
        print("say  it again please:>>>>>")
        return "None"
    return query


if __name__ == "__main__":
    # speak("mukesh is a good boy")
    wishme()

    if 1:
        query = takecommand().lower()
    #  logic
        if "wikipedia" in query:
            speak("searching wikipedia...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            speak(f"according to wikipedia {result}")
        elif "open youtube" in query:
            webbrowser.open("youtube.com")
        elif "open google" in query:
            webbrowser.open("google.com")
        elif "open photo" in query:
            loc = "C:\\Users\\mukes\\OneDrive\\Pictures\\Screenshots"
            try:
                photo = os.listdir(loc)
                rand = choice(photo)
            # print(photo)
            except Exception as e:
                exit()
            os.startfile(os.path.join(loc, rand))
        elif "the time" in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir the  time is  {strtime}")
        elif "open vscode" or "open code" in query:
            pathpfcode = "C:\\Users\\mukes\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            try:
                os.startfile(pathpfcode)
            except Exception as e:
                exit()

        # elif "open instagram" or "open insta" in query:
        #     instapath = "C:\\Program Files (x86)\\Microsoft\Edge\\Application\\msedge_proxy.exe"
        #     os.startfile(instapath)
        else:
            exit()
    else:
        exit()
