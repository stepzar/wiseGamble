from collectingData.utils import retrieveMatchesByDate, retrieveMatchById
from data.beans.Partita import Partita
from data.dao.PartitaDao import PartitaDao
from datetime import datetime

class PartitaDaoSofascore(PartitaDao):
    def doRetrieveById(self, id: int):
        return retrieveMatchById(id)

    def doUpdate(self, partita: Partita):
        return

    def doDelete(self, partita: Partita):
        return

    def doRetriveAll(self):
        partite = retrieveMatchesByDate(datetime.today().strftime('%Y-%m-%d'))
        return partite

    def doRetrieveByDate(self, date):
        if date == "":
            return PartitaDaoSofascore.doRetriveAll()
        else:
            return retrieveMatchesByDate(date)