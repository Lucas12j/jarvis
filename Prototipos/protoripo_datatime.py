from datetime import date,time,datetime,timezone
import time

while True:

    a=date.today()
    b=datetime.now()
    print(str(a.day)+"/"+str(a.month)+"/"+str(a.year))
    print(str(b.hour-3)+":"+str(b.minute)+":"+str(b.second))
    time.sleep(1)
