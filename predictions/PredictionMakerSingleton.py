from predictions.PredictionMaker import PredictionMaker
from predictions.Predictor import Predictor
from joblib import load
from sklearn import preprocessing
import numpy as np

predictionMaker = PredictionMaker()
encoder = preprocessing.LabelEncoder()
encoder.classes_ = np.load('predictions/fileimport/encoder.npy')


predictorYellowCard = Predictor("YellowCards", classificatore=load('predictions/fileimport/yellowcardsOvUn55.joblib'), scaler= load('predictions/fileimport/scaler_yellowcardsOvUn55.joblib'), encoder=encoder ,mappingOfResults={0: "Under 5.5",1:"Over 5.5"}, columns=["tournament_name", "country", "referee", "homeTeam_id", "awayTeam_id", "all_shots_on_target_home", "all_fouls_home", "all_fouls_away", "all_yellow_cards_home", "all_yellow_cards_away"])
predictorCorner = Predictor("Corner", classificatore=load('predictions/fileimport/cornerovun75.joblib'), scaler=load('predictions/fileimport/scaler_cornerovun75.joblib'), encoder=encoder, mappingOfResults={0: "Under 7.5", 1: "Over 7.5"}, columns=["timestamp", "country", "all_ball_possession_away", "all_shots_on_target_home","all_shots_off_target_home","all_corner_kicks_home","all_corner_kicks_away", "all_goalkeeper_saves_away", "people_vote_x", "people_vote_2"])

predictionMaker.addPredictor(predictorYellowCard)
predictionMaker.addPredictor(predictorCorner)