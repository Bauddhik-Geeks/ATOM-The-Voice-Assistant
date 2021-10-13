import libraries as lb
from Text import colorText
from wish import wish
from binstar_client.inspect_package import r
from numpy.lib.utils import source

import pyjokes  # pip install pyjokes
import datetime
import pyjokes #pip install pyjokes



lb.os.system("cls")

# ASCII file
f = open("Ascii.txt", "r")
ascii = "".join(f.readlines())
print(colorText(ascii))

lb.pyttsx3.speak("Enter your password")
inpass = lb.getpass.getpass("Enter your password :")
apass = "nitesh"
if inpass != apass:
    lb.pyttsx3.speak("Incorrect Password Try Again ")
    exit()
    print("Access Granted")
lb.pyttsx3.speak("Access Granted")

# sapi5 is speech API developed by Microsoft, helps in synthesis and recognition of voice
api = lb.pyttsx3.init('sapi5')
voices = api.getProperty("voices")  # getting detail of current voice
api.setProperty('voice', voices[0].id)


def speak(audio):
    api.say(audio)
    api.runAndWait()


def jokes():
    speak(pyjokes.get_joke())


def Introduction():
    speak("I am ATOM , AI assistant"
          "Created by Nitesh,"
          "I can help you in various regards,"
          "I can search for you on the Internet,"
          "I can also grab definitions for you from wikipedia,"
          "I am always happy to help you!,")


def takecommand():  # It rakes microphone input from the user and returns string output
    r = lb.sr.Recognizer()
    with lb.sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1  # take 1 sec after command is ececuted
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"Me: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query


if __name__ == "__main__":
    wish()
    print("I am Atom, Please tell me how can I help you")
    lb.pyttsx3.speak("I am Atom, Please tell me how can I help you")
    while True:
        query = takecommand().lower()
        if query == 0:
            continue

        if "sign out" in query:
            break

        ############################WIKIPEDIA####################################

        if 'wikipedia' in query:
            lb.pyttsx3.speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            # return 2 sentence from wikipedia
            results = lb.wikipedia.summary(query, sentences=2)
            lb.pyttsx3.speak("According to wikipedia")
            print(results)
            lb.pyttsx3.speak(results)

        ##########################Task that Atom can do ####################
        elif 'task' in query:
            print("I can play song, open websites, search wikipediam, can tell about weather and I can work on AWS cloud and Linux")
            lb.pyttsx3.speak(
                "I can play song, open websites, search wikipediam, can tell about weather and I can work on AWS cloud and Linux")

        ############################### TIME #################################
        elif 'time' in query:
            Time = lb.datetime.datetime.now().strftime("%H:%M:%S")
            lb.pyttsx3.speak(f"the time is {Time}")

        ################################## weather###########################
        elif 'weather' in query:
            api_key = "8ef61edcf1c576d65d836254e11ea420"
            base_url = "https://api.openweathermap.org/data/2.5/weather?"
            lb.pyttsx3.speak("whats the city name")
            city_name = takecommand()
            complete_url = base_url + "appid=" + api_key + "&q=" + city_name
            response = lb.requests.get(complete_url)
            x = response.json()
            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                lb.pyttsx3.speak(" Temperature in kelvin unit is " +
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

        ############################### GREET#########################
        elif 'hello' in query:
            greetings = [
                f"hello sir,nice to see you",
                f"welcome sir, how can i help you"]
            greet = greetings[lb.random.randint(0, len(greetings) - 1)]
            lb.pyttsx3.speak(greet)

        ############################## Search ########################

        elif 'search' in query:
            ##driver = lb.webdriver.Chrome()
            index = query.lower().split().index('search')
            query = query.split()[index + 1:]
            lb.driver.get(
                "https://www.google.com/search?q =" + '+'.join(query))

        ######################## Search Youtube ########################

        elif 'youtube' in query:    # Ask: Search for Avengers on Youtube
            search_term = query.split('for')[-1].split('on')[0].strip()
            url = f'https://www.youtube.com/results?search_query={search_term}'
            lb.webbrowser.get().open(url)
            lb.pyttsx3.speak(
                f'Here is what I found for {search_term} on youtube')

        ######################## Search Location ########################

        elif 'location' in query:   # Ask: Find location
            lb.pyttsx3.speak('What is the location?')
            location = takecommand()
            url = 'https://google.nl/maps/place/' + location + '/&amp;'
            lb.webbrowser.get().open(url)
            lb.pyttsx3.speak('Here is the location for ' + location)

        ######################### Jokes ###############################
        elif 'joke' in query:
            jokes()

        ########################## Introduction ############################
        elif 'tell me about yourself' and 'who are you' in query:
            Introduction()

        
        ########################### NOTE #############################

        elif "write a note" in query:
            lb.pyttsx3.speak("What should i write, sir")
            note = takecommand()
            file = open('notes.txt', 'a')
            lb.pyttsx3.speak("Sir, Should i include date and time")
            snfm = takecommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = str(datetime.datetime.now())
                file.write(strTime)
                file.write(" :- ")
                file.write(f'{note}\n')
                file.close()
            else:
                file.write(f'{note}\n') 
                file.close()

        elif "show note" in query:
            lb.pyttsx3.speak("Showing notes on terminal.")
            file = open("notes.txt", "r")
            print(file.read())


       

        ########################## Date ####################################
        elif 'date' in query:
            tday = lb.datetime.date.today()
            print('Todays Date is ', tday)
            lb.pyttsx3.speak('Todays Date is ')
            lb.pyttsx3.speak(tday)
            print('Do you want me to remember a specific date?')
            lb.pyttsx3.speak('Do you want me to remember a specific date?')
            ask_q = takecommand().lower()
            if 'no' in ask_q:
                continue
            elif 'yes' or 'yeah' in ask_q:
                lb.pyttsx3.speak('Kindly Tell me the date you want me to set')
                dt = takecommand().lower()
                if dt != 'none':
                    print('Important Date is ', dt)
                    lb.pyttsx3.speak('Important Date is ')
                    lb.pyttsx3.speak(dt)
                    with open('important_dates.csv', 'a') as f:
                        f.write(dt)
                        f.write('\n')
                    f.close()
                    lb.pyttsx3.speak('okay date set')
            else:
                continue
