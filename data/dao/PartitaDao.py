from abc import abstractmethod,ABC

from data.beans.Partita import Partita


class PartitaDao(ABC):
    @abstractmethod
    def doSave(self, partita: Partita):
        pass

    @abstractmethod
    def doRetrieveAll(self):
        pass

    @abstractmethod
    def doRetrieveById(self, id : int):
        pass