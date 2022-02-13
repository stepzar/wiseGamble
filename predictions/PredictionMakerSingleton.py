from predictions.PredictionMaker import PredictionMaker
from predictions.Predictor import Predictor

predictionMaker = PredictionMaker()
##importare i classificatori da collab

##esempio con un classificatore finto
def mock():
    pass
mockClassifier = mock
mockClassifier.predict = lambda x: 1
mockPredictor = Predictor("1X2", mockClassifier, {0: "1", 1: "X", 2: "2"})
predictionMaker.addPredictor(mockPredictor)
