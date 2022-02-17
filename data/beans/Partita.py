class Partita:

    def __init__(self, id, nomeCasa, nomeFuoriCasa, dataIncontro, league, home_image, away_image, home_df, away_df):
        self.id = id
        self.home = nomeCasa
        self.away = nomeFuoriCasa
        self.date = dataIncontro
        self.league = league
        self.home_image = home_image
        self.away_image = away_image
        self.home_df = home_df
        self.away_df = away_df