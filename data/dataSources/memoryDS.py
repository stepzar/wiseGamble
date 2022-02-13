from data.beans.Partita import Partita
from datetime import datetime

memoryDS = {}

#Riempi memoryDS di partite di oggi prese da sofaScore


##esempio
partita = Partita(1,"Napoli","Juventus",datetime(2020,12,25,18,30))
partita2 = Partita(2,"Napoli","Milan",datetime(2021,12,25,18,30))
memoryDS[partita.id] = partita
memoryDS[partita2.id] = partita2