from abc import abstractmethod,ABC

from data.beans.Partita import Partita


class PartitaDao(ABC):

    @abstractmethod
    def doRetriveAll(self):
        pass

    @abstractmethod
    def doRetrieveById(self,id : int):
        pass

    @abstractmethod
    def doUpdate(self,partita : Partita):
        pass
    @abstractmethod
    def doDelete(self,partita : Partita):
        pass