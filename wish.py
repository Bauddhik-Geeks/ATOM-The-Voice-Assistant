import libraries as lb

#Wishes according to the time
def wish():
    hour=lb.datetime.datetime.now().hour #now() use to tell the current time
    if hour>=0 and hour<12:
        lb.pyttsx3.speak("Hello,Good Morning")
        print("Hello,Good Morning")
    elif hour>=12 and hour<18:
        lb.pyttsx3.speak("Hello,Good Afternoon")
        print("Hello,Good Afternoon")
    else:
        lb.pyttsx3.speak("Hello,Good Evening")
        print("Hello,Good Evening")