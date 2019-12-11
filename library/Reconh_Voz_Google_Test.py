import speech_recognition as sr
import os

class Captar_voz():
    def __init__(self):
        self.r = sr.Recognizer()

    def captar_voz(self):
      
        with sr.Microphone() as s:
            self.r.adjust_for_ambient_noise(s)
            audio = self.r.listen(s)
            try:
                if os.name == 'nt':
                    os.system("cls")
                else:
                    os.system("clear")
                return(self.r.recognize_google(audio, language='pt'))
            except:
                return("ERRO1997")
 