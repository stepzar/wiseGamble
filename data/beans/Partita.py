class Partita:

    def __init__(self, id, nomeCasa, nomeFuoriCasa, timestamp, tournament_name, home_image, away_image,
                referee, homeTeam_id, awayTeam_id,country, all_fouls_home, all_fouls_away,
                all_yellow_cards_home, all_yellow_cards_away, all_ball_possession_away,
                all_shots_on_target_home,  all_shots_off_target_home, all_corner_kicks_home,
                all_corner_kicks_away, all_goalkeeper_saves_away, people_vote_x, people_vote_2):
        self.id = id
        self.home = nomeCasa
        self.away = nomeFuoriCasa
        self.timestamp = timestamp
        self.tournament_name = tournament_name
        self.home_image = home_image
        self.away_image = away_image
        self.referee = referee
        self.homeTeam_id = homeTeam_id
        self.awayTeam_id = awayTeam_id
        self.country = country
        self.all_fouls_home = all_fouls_home
        self.all_fouls_away = all_fouls_away
        self.all_yellow_cards_home = all_yellow_cards_home
        self.all_yellow_cards_away = all_yellow_cards_away
        self.all_ball_possession_away = all_ball_possession_away
        self.all_shots_on_target_home = all_shots_on_target_home
        self.all_shots_off_target_home = all_shots_off_target_home
        self.all_corner_kicks_home = all_corner_kicks_home
        self.all_corner_kicks_away = all_corner_kicks_away
        self.all_goalkeeper_saves_away = all_goalkeeper_saves_away
        self.people_vote_x = people_vote_x
        self.people_vote_2 = people_vote_2


    def __str__(self):
        return str(self.__dict__)