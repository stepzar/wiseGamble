from data.beans.Partita import Partita
from predictions.Predictor import Predictor


class PredictionMaker:

    def __init__(self):
        self.predictors = []

    def addPredictor(self,predictor : Predictor):
        self.predictors.append(predictor)

    def makePredictions(self,partita : Partita) -> dict:
        result = {}
        for predictor in self.predictors:
            predictionResult = predictor.predictPartita(partita)
            result[predictionResult[0]] = predictionResult[1]
        return result
