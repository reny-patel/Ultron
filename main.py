import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[2].id)
engine.setProperty('rate', 190)
engine.setProperty('volume',1.0)


def talk(text):
    engine.say(text)
    engine.runAndWait()




def run_ultron():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)

    elif 'search for' in command:
        person = command.replace('search for ', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)

    elif 'Tell me something about you' in command:
        talk('I am Ultron, your personal virtual assistant. An AI based application program that understands natural language voice commands and completes tasks for the user.')

    elif 'joke' in command:
        talk(pyjokes.get_joke())

    else:
        talk('Please say the command again.')


def take_command():
    try:
        with sr.Microphone() as source:
            talk('HI guys. How may I help you?')
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'ultron' in command:
                command = command.replace('ultron', '')
                print(command)
    except:
        pass
    return command


while True:
    run_ultron()