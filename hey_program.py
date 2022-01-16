






import pyttsx3    
import webbrowser   
import speech_recognition as sr
import datetime
 
# init function to get an engine instance for the speech synthesis 
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 178)

#print=sg.Print
name = input("enter your name---> ")


def wishMe(name):
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak(f"Good Morning!{name}")

    elif hour>=12 and hour<18:
        speak(f"Good Afternoon!{name}")   

    else:
        speak(f"Good Evening!{name}")  

    #engine.say(. Please tell me how may I help you")       


def speak(audio): 
    engine.say(audio) 
    engine.runAndWait() 

def takeCommand():
      
    r = sr.Recognizer()
      
    with sr.Microphone() as source:
        print ('\U0001F600')
        print("Listening...") 
        r.energy_threshold = 500
        r.pause_threshold = 0.7
        r.non_speaking_duration = 0.2        
        audio = r.listen(source)
    
    try: 
        print("Recognizing...")     
        query = r.recognize_google(audio, language ='en-in') 
        print(f"User said: {query}\n") 
    
    except Exception as e: 
        print(e)
        #print("Unable to Recognizing your voice.")
        #speak("Sorry, I didn't get that.")
        return "None"

    return query 

if __name__ == '__main__': 
    wishMe(name)
    query=takeCommand().lower()
    while True : 
        query=takeCommand().lower()
        if 'program' in query : 
            print('in')
            speak('i am online')
            while True:
                query=takeCommand().lower()
                if 'help'in query : 
                    speak('ok what a question.')
                    print ('\U0001F607')
                    while True:
                        r = sr.Recognizer()
                        with sr.Microphone() as source:
                            print ('\U0001F600')
                            print("Listening...") 
                            r.energy_threshold = 500
                            r.pause_threshold = 0.7
                            r.non_speaking_duration = 0.2        
                            audio = r.listen(source)
    
                            try: 
                                print("Recognizing...")     
                                find1 = r.recognize_google(audio, language ='en-in') 
                                #print(f"User said: {query}\n") 
                                webbrowser.open(f'https://www.google.com/search?q={find1}')
                                speak(f'i got it {find1}')   
            
                            except Exception as e: 
                                print(e)
                                
                            if 'ok go back' in find1:
                                speak('i got it lets go back')
                                break
                elif 'open youtube'in query : 
                    speak('ok we are in youtube.')
                    print ('\U0001F607')
                    while True:
                        r = sr.Recognizer()
                        with sr.Microphone() as source:
                            print ('\U0001F600')
                            print("Listening...") 
                            r.energy_threshold = 500
                            r.pause_threshold = 0.7
                            r.non_speaking_duration = 0.2        
                            audio = r.listen(source)
    
                            try: 
                                print("Recognizing...")     
                                find1 = r.recognize_google(audio, language ='en-in') 
                                #print(f"User said: {query}\n") 
                                webbrowser.open(f'https://www.youtube.com/results?search_query={find1}')
                                speak(f'i got it {find1}')   
            
                            except Exception as e: 
                                print(e)
                                
                            if 'ok go back' in find1:
                                speak('i got it lets go back')
                                break    
                if 'sleep' in query : 
                    speak('i got it\n ok i am going to sleep')
                    break    
        if 'bye' in query : 
            print(f'ok bye {name}')
            break
    
