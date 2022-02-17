from collectingData.utils import retrieveMatchesByDateSofascore, retrieveMatchByIdSofascore
from data.beans.Partita import Partita
from data.dao.PartitaDao import PartitaDao
from datetime import datetime
import sqlite3

leagues = {
    "champions":"UEFA Champions League",
    "europa":"UEFA Europa League",
    "premier":"Premier League",
    "laliga":"LaLiga",
    "bundesliga":"Bundesliga",
    "seriea":"Serie A",
    "ligue1":"Ligue 1",
    "eredivise":"Eredivise",
    "premiership":"Premiership",
    "serieb":"Serie B",
    "proleague":"Pro League",
    "superliga":"Superliga",
    "championship":"Championship",
    "eliteserien":"Eliteserien",
    "lechpozann":"Lech pozann",
}

class PartitaDaoSofascore(PartitaDao):
    def __init__(self):
        self.connection = sqlite3.connect("database.db", check_same_thread=False)
        self.cur = self.connection.cursor()
        """
        with open('schema.sql', 'r') as f:
            self.connection.executescript(f.read())

        # initialize db with today matches on sofascore
        for match in retrieveMatchesByDateSofascore(datetime.today().strftime('%Y-%m-%d')):
            self.doSave(retrieveMatchByIdSofascore(match))
        """
    def doSave(self, partita: Partita):
        self.cur.execute("INSERT INTO partita (id , home, away, timestamp, tournament_name, home_image, away_image, referee, homeTeam_id, awayTeam_id, country, all_fouls_home, all_fouls_away, all_yellow_cards_home, all_yellow_cards_away, all_ball_possession_away, all_shots_on_target_home, all_shots_off_target_home, all_corner_kicks_home, all_corner_kicks_away, all_goalkeeper_saves_away, people_vote_x, people_vote_2) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (partita.id , partita.home, partita.away, partita.timestamp, partita.tournament_name, partita.home_image, partita.away_image, partita.referee, partita.homeTeam_id, partita.awayTeam_id,partita.country, partita.all_fouls_home, partita.all_fouls_away, partita.all_yellow_cards_home, partita.all_yellow_cards_away, partita.all_ball_possession_away, partita.all_shots_on_target_home, partita.all_shots_off_target_home, partita.all_corner_kicks_home, partita.all_corner_kicks_away, partita.all_goalkeeper_saves_away, partita.people_vote_x, partita.people_vote_2))
        self.connection.commit()

    def doRetrieveById(self, id: int):
        partita = self.cur.execute("SELECT * FROM partita where id = ?", (id,)).fetchone()
        return self.sqlToPartita(partita)

    def doRetrieveAll(self):
        partite = self.cur.execute("SELECT * FROM partita").fetchall()
        matches = []
        for partita in partite:
            matches.append(self.sqlToPartita(partita))

        return matches

    def doRetrieveByLeague(self, league):
        partite = self.cur.execute("SELECT * FROM partita where tournament_name = ?", (leagues[league],)).fetchall()
        matches = []
        for partita in partite:
            matches.append(self.sqlToPartita(partita))

        return matches

    def sqlToPartita(self,tupla):
        return Partita(*tupla)