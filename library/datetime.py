from datetime import date,time,datetime,timezone

class Datetime():

    def __init__(self):
         self.data=date.today()
         self.hora=datetime.now()

    def getData(self):
        return str(self.data.day)+"/"+str(self.data.month)+"/"+str(self.data.year)
    
    def getHora(self):
        return str(self.hora.hour-3)+":"+str(self.hora.minute)+":"+str(self.hora.second)  

        #Devido ao meu dual boot, no windows as horas ficam erradas, com uma diferença de 3 horas a mais.
        