from predictions.PredictionMaker import PredictionMaker
from predictions.Predictor import Predictor
from joblib import load
from sklearn import preprocessing
import numpy as np

predictionMaker = PredictionMaker()
encoder = preprocessing.LabelEncoder()
encoder.classes_ = np.load('/fileimport/encoder.npy')


predictorYellowCard = Predictor("YellowCards", classificatore=load('/fileimport/yellowcardOvUn55.joblib'), scaler= load('predictions/fileimport/scaler_yellowcardsOvUn55.joblib'), encoder=encoder ,mappingOfResults={0: "Under",1:"Over"}, columns=["timestamp", "country", "all_ball_possession_away", "all_shots_on_target_home","all_shots_off_target_home","all_corner_kicks_home","all_corner_kicks_away", "all_goalkeeper_saves_away", "people_vote_x", "people_vote_2"])
predictorCorner = Predictor("Corner", classificatore=load('/fileimport/cornerovun75.joblib'), scaler=load('predictions/fileimport/scaler_cornerovun75.joblib'), encoder=encoder, mappingOfResults={0: "Under", 1: "Over"}, columns=[])

predictionMaker.addPredictor(predictorYellowCard)
predictionMaker.addPredictor(predictorCorner)