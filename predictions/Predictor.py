import pandas

from data.beans.Partita import Partita
from pandas.core.frame import DataFrame


class Predictor:

    def __init__(self, outputName, classificatore, scaler, encoder, mappingOfResults,columns):
        self.outputName = outputName
        self.classificatore = classificatore
        self.scaler = scaler
        self.encoder = encoder
        self.mappingOfResults = mappingOfResults
        self.columns = columns

    def predictPartita(self, partita : Partita):
        df = self.createDataframe(partita)
        self.encoding(df)
        df = self.scaling(df)
        df = df[self.columns]
        prediction = self.classificatore.predict(df)
        prediction = prediction[0]
        return (self.outputName, self.mappingOfResults[prediction])

    def encoding(self, df):
        if("tournament_name" in df.columns):
            df["tournament_name"] = self.encoder.fit_transform(df.tournament_name)
        if ("country" in df.columns):
            df["country"] = self.encoder.fit_transform(df.country)
        if ("referee" in df.columns):
            df["referee"] = self.encoder.fit_transform(df.referee)

    def scaling(self, df):
        df_scaling = self.scaler.transform(df)
        df_scaling = DataFrame(df_scaling, columns=df.columns)
        return df_scaling

    def createDataframe(self, partita):
        cols = ['timestamp', 'tournament_name', 'country', 'round', 'city', 'stadium',
       'referee', 'homeTeam_id', 'awayTeam_id', 'all_ball_possession_home',
       'all_ball_possession_away', 'all_shots_on_target_home',
       'all_shots_on_target_away', 'all_shots_off_target_home',
       'all_shots_off_target_away', 'all_corner_kicks_home',
       'all_corner_kicks_away', 'all_fouls_home', 'all_fouls_away',
       'all_yellow_cards_home', 'all_yellow_cards_away',
       'all_goalkeeper_saves_home', 'all_goalkeeper_saves_away',
       'people_vote_1', 'people_vote_x', 'people_vote_2', 'id_manager_home',
       'id_manager_away']
        df = pandas.DataFrame({k : [0] for k in cols })
        for col in self.columns:
            df.loc[0,col] = partita.__dict__[col]
        #df = pandas.DataFrame({k: [v] for k, v in partita.__dict__.items()})
        #return df[self.columns]
        return df

