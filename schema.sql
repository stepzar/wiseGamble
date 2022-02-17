DROP TABLE IF EXISTS partita;

CREATE TABLE partita (
    id INTEGER PRIMARY KEY,
    home TEXT,
    away TEXT,
    timestamp INTEGER,
    tournament_name TEXT,
    home_image TEXT,
    away_image TEXT,
    referee TEXT,
    homeTeam_id INT,
    awayTeam_id INT,
    country TEXT,
    all_fouls_home REAL,
    all_fouls_away REAL,
    all_yellow_cards_home REAL,
    all_yellow_cards_away REAL,
    all_ball_possession_away REAL,
    all_shots_on_target_home REAL,
    all_shots_off_target_home REAL,
    all_corner_kicks_home REAL,
    all_corner_kicks_away REAL,
    all_goalkeeper_saves_away REAL,
    people_vote_x REAL,
    people_vote_2 REAL
)