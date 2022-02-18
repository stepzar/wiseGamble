from collectingData.utils import retrieveMatchesByDateSofascore, retrieveMatchByIdSofascore
import datetime
from data.dao.memoryImpl.PartitaDaoSofascore import PartitaDaoSofascore

if __name__ == "__main__":

    dao = PartitaDaoSofascore()

    with open('../schema.sql', 'r') as f:
        dao.connection.executescript(f.read())

    date = datetime.datetime.today()

    # initialize db with date matches on sofascore
    for match in retrieveMatchesByDateSofascore(date.strftime('%Y-%m-%d')):
        dao.doSave(retrieveMatchByIdSofascore(match))
        print(f"Partita salvata {match}")

    dao.closeConnection()