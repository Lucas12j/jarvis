from datetime import date,time,datetime,timezone

class Datetime():

    def __init__(self):
         self.data=date.today()
         self.hora=datetime.now()

    def getData(self):
        return str(self.data.day)+" do "+str(self.data.month)+" de "+str(self.data.year)
    
    def getHora(self):
        return str(self.hora.hour)+" horas e "+str(self.hora.minute)+" minutos "
