from data.beans.Partita import Partita
from data.dao.PartitaDao import PartitaDao
from data.dataSources.memoryDS import memoryDS

class PartitaDaoMemory(PartitaDao):
    def doRetrieveById(self, id: int):
        return memoryDS[id]

    def doUpdate(self, partita: Partita):
        memoryDS[partita.id] = partita

    def doDelete(self, partita: Partita):
        del memoryDS[partita.id]

    def doRetriveAll(self):
        return list(memoryDS.values())