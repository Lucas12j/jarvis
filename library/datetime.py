from datetime import date,time,datetime,timezone

class Datetime():

    def __init__(self):
         self.data=date.today()
         self.hora=datetime.now()

    def getData(self):
        return str(self.data.day)+"/"+str(self.data.month)+"/"+str(self.data.year)
    
    def getHora(self):
        return str(self.hora.hour)+":"+str(self.hora.minute)+":"+str(self.hora.second)  

        