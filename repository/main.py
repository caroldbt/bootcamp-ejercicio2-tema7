from datetime import datetime
from time import time, strftime, gmtime


hour=strftime("%H")
minutes=strftime("%M")
print("Hora actual: ",hour,":",minutes)
if int(hour)>19:
    print("Ya son mas de las 7 finaliza la jornada.")
else:
    print("El tiempo que queda de trabajo es: ",18-int(hour),"horas",59-int(minutes),"minutos")
