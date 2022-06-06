from multiprocessing.connection import Listener
from PyQt5.QtWidgets import *

from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
import speech_recognition as sr
import pyaudio 
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import cv2
import sys
import time
import phonenumbers

from phonenumbers import geocoder
from phonenumbers import carrier

Listener=sr.Recognizer()
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
        try:
            with sr.Microphone() as source:
                print("listening...")
                voice=Listener.listen(source,timeout=2)
                command=Listener.recognize_google(voice)
                command=command.lower()
                if 'veronica' in command:
                   command=command.replace('hi','')
                   command=command.replace('hey','')
                   command=command.replace('veronica','')
                   command=command.replace(' ','')
                   print(command)
        except:
                talk('please repeat the command')    
                command=take_command()
            
        return command



def run_veronica():
    command=take_command()
    print(command)
    if 'play' in command:
        song=command.replace('play','')
        talk('playing'+song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time=datetime.datetime.now().strftime('%I:%M %p')
        talk('current time is'+time)
    elif 'who is ' in command:
        person=command.replace('who is','')
        info=wikipedia.summary(person,5)
        talk(info)
    elif ' date ' in command:
        talk('i am sakt londa  ')
    elif 'are you single' in command:
        talk('i am in relationship with python ')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'whatsapp' in command:
        command=take_command()
        command=command.replace('send message','')
        c=input("enter the no:")
        t=int(input("enter the time in hr: "))
        t2=int(input("enter the time in min "))
        pywhatkit.sendwhatmsg(c,command,t,t2,15,True)
    elif 'camera' in command:
        cam=cv2.VideoCapture(0)
        while cam.isOpened():
            ret,frame1=cam.read()
            if cv2.waitKey(1)==ord('q'):
                break
            cv2.imshow('Security Cam',frame1)
    elif 'browser' in command:
        class MainWindow(QMainWindow):
            def _init_(self):
                super(MainWindow,self)._init_()
                self.browser = QWebEngineView()
                self.browser.setUrl(QUrl('http://google.com'))
                self.setCentralWidget(self.browser)
                self.showMaximized()
                navbar=QToolBar()
                self.addToolBar(navbar)
                backbtn=QAction('Back',self)
                backbtn.triggered.connect(self.browser.back)
                navbar.addAction(backbtn)
                frontbtn=QAction('Front',self)
                frontbtn.triggered.connect(self.browser.forward)
                navbar.addAction(frontbtn)
                reloadbtn=QAction('Reoload',self)
                reloadbtn.triggered.connect(self.browser.reload)
                navbar.addAction(reloadbtn)
                homebtn=QAction('Home',self)
                homebtn.triggered.connect(self.khome)
                navbar.addAction(homebtn)

            def khome(self):
                self.browser.setUrl(QUrl('http://google.com'))
        app=QApplication(sys.argv)
        QApplication.setApplicationName('Interent')
        window = MainWindow()
        app.exec_()
    elif 'location' in command:
        number=(input("enter the no:"))
        ch_no=phonenumbers.parse(number,"ch")
        print(geocoder.description_for_number(ch_no,"en"))
        ser_no=phonenumbers.parse(number,"ro")
        print(carrier.name_for_number(ser_no,"en"))
    elif 'exit' in command:
        talk('thanks have a good day')
        exit()
    else :
        talk('oops something went wrong ')
time.sleep(0)
talk('how can i help you')
while 1:
    run_veronica()