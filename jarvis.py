import speech_recognition as sr   # type: ignore
import pyttsx3  # type: ignore
import webbrowser
import datetime
import pyjokes # type: ignore

"""first we create function then create variable and call our Recognizer class with source microphone function 
1)they are both the part of speech_recognition module or also library in broder sense
2)now there will also be noise so in order to avoid the noise cancletion we write the line1 below  """ 

def sptext():
    recognizer=sr.Recognizer()
    with sr.Microphone() as source:
        print(".....listening.....")
        recognizer.adjust.for_ambient_noise(source)#line1
        audio=recognizer.listen(source)
        try:
            print("recognizing......")
            data=recognizer.recognize_google(audio)
            print(data)
        except sr.UnKnownValueError:
            print("Not understand ")

sptext()    


#this function will convert speech to text
def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Adjusting for ambient noise...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        print("Say something!")
        audio = recognizer.listen(source)
    try:
        data= recognizer.recognize_google(audio)
        print(data)
        return data
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

sptext()


#now we will creat the function that will convert the text to speech 
# # #first calling the class of pyttsx3

def textsp(x):
    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    rate=engine.getProperty('rate')
    engine.setProperty('rate',100)
    engine.say(x)
    engine.runAndWait()

# textsp("hello well i will  get my dream car and i dont know what i am doing but i will win ")

if __name__ == '__main__' :
    # if sptext().lower()=="hey peter":
        data1=sptext().lower()
        if "your name" in data1:
             name="my name is  skinny seema "
             textsp(name)
