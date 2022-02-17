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
        print("partita df " , partita.df)
        self.encoding(partita.df)
        print("partita df dopo encoding ", partita.df)
        df = self.scaling(partita.df)
        print("partita df dopo scaling ", df)
        prediction = self.classificatore.predict(df)
        prediction = prediction[0]
        return (self.outputName, self.mappingOfResults[prediction])

    def encoding(self, df):
        df["tournament_name"] = self.encoder.fit_transform(df.tournament_name)
        df["country"] = self.encoder.fit_transform(df.country)
        df["city"] = self.encoder.fit_transform(df.city)
        df["stadium"] = self.encoder.fit_transform(df.stadium)
        df["referee"] = self.encoder.fit_transform(df.referee)
        df["home_formation"] = self.encoder.fit_transform(df.home_formation)
        df["away_formation"] = self.encoder.fit_transform(df.away_formation)

    def scaling(self, df):
        df_scaling = self.scaler.transform(df)
        df_scaling = DataFrame(df_scaling, columns=df.columns)
        return df_scaling