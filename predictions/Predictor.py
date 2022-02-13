from data.beans.Partita import Partita


class Predictor:

    def __init__(self,outputName,classificatore,mappingOfResults):
        self.outputName = outputName
        self.classificatore = classificatore
        self.mappingOfResults = mappingOfResults

    def predictPartita(self,partita:Partita):
        prediction = self.classificatore.predict(partita.stats) #penso si debba fare sicuramente qualche lavoro di preprocessing
        return (self.outputName,self.mappingOfResults[prediction])