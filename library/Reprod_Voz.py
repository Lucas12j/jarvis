import pyttsx3

class Reprod_Voz():

    def __init__(self, fala):
        self.engine = pyttsx3.init()
        self.engine.setProperty('voice','pt')
        self.engine.setProperty('rate',130)
        self.engine.setProperty('volume',1.0)
        self.fala = fala
    
    def reproduzir(self):
        self.engine.say(self.fala)
        self.engine.runAndWait()


