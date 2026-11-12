
CREATE TABLE IF NOT EXISTS Seasons (
    season CHAR(9) PRIMARY KEY, -- E.g., 2023-2024
    season_start_date CHAR(10) NOT NULL, -- Format: yyyy-MM-dd. Default to 1st of August
    season_end_date CHAR(10) NOT NULL -- Default to 30th of June
);

CREATE TABLE IF NOT EXISTS Teams (
    fpl_team_code INT PRIMARY KEY,
    team_name VARCHAR(255) NOT NULL,
    short_name CHAR(3) NOT NULL,
    transfermarkt_team_name VARCHAR(255),
    transfermarkt_team_id INT,
    understat_team_name VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS Players (
    fpl_player_code INT PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    second_name VARCHAR(255) NOT NULL,
    transfermarkt_player_name VARCHAR(255),
    transfermarkt_player_id INT,
    understat_player_id INT
);

CREATE TABLE IF NOT EXISTS Season_Teams (
    season CHAR(9) NOT NULL REFERENCES Seasons(season) ON DELETE CASCADE,
    fpl_team_code INT NOT NULL REFERENCES Teams(fpl_team_code) ON DELETE CASCADE,
    season_fpl_team_id INT NOT NULL,

    PRIMARY KEY (season, fpl_team_code)
);

CREATE TABLE IF NOT EXISTS Season_Players (
    season CHAR(9) NOT NULL REFERENCES Seasons(season) ON DELETE CASCADE,
    fpl_player_code INT NOT NULL REFERENCES Players(fpl_player_code) ON DELETE CASCADE,
    season_fpl_player_id INT NOT NULL,
    fpl_position CHAR(3) NOT NULL,

    PRIMARY KEY (season, fpl_player_code)
);

CREATE TABLE IF NOT EXISTS Squad_Player_Registrations (
    registration_id INT PRIMARY KEY,
    fpl_player_code INT NOT NULL REFERENCES Players(fpl_player_code) ON DELETE CASCADE,
    fpl_team_code INT NOT NULL REFERENCES Teams(fpl_team_code) ON DELETE CASCADE,
    team_join_date CHAR(10) NOT NULL, -- Format: yyyy-MM-dd
    team_leave_date CHAR(10) -- NULL means player is still registered for this team.
);

CREATE TABLE IF NOT EXISTS Fixtures (
    fpl_fixture_code INT PRIMARY KEY,
    season CHAR(9) NOT NULL REFERENCES Seasons(season) ON DELETE CASCADE,
    home_team_code INT NOT NULL REFERENCES Teams(fpl_team_code) ON DELETE CASCADE,
    away_team_code INT NOT NULL REFERENCES Teams(fpl_team_code) ON DELETE CASCADE,
    finished INT NOT NULL DEFAULT 0 CHECK (finished IN (0, 1)),
    gameweek INT NOT NULL,
    season_fpl_fixture_id INT NOT NULL,
    kickoff_date CHAR(10) NOT NULL, -- Format: yyyy-MM-dd
    kickoff_time CHAR(8) NOT NULL, -- Format: hh:mm:ss
    home_team_score INT, -- NULL means score not recorded yet (game hasn't happened yet).
    away_team_score INT,
    home_team_expected_goals REAL,
    away_team_expected_goals REAL
);

CREATE TABLE IF NOT EXISTS Player_Match_Info(
    fpl_player_code INT NOT NULL REFERENCES Players(fpl_player_code) ON DELETE CASCADE,
    fpl_fixture_code INT NOT NULL REFERENCES Fixtures(fpl_fixture_code) ON DELETE CASCADE,
    fpl_price INT NOT NULL, -- E.g., "70" is £7.0m.
    played INT NOT NULL DEFAULT 0 CHECK (played IN (0, 1)),
    injured INT NOT NULL DEFAULT 0 CHECK (injured IN (0, 1)),
    suspended INT NOT NULL DEFAULT 0 CHECK (suspended IN (0, 1)),
    mins_played INT NOT NULL,
    goals INT NOT NULL,
    expected_goals REAL NOT NULL,
    shots INT NOT NULL,
    penalties_missed INT NOT NULL,
    assists INT NOT NULL,
    expected_assists REAL NOT NULL,
    tackles INT NOT NULL,
    recoveries INT NOT NULL,
    clearances_blocks_interceptions INT NOT NULL,
    goals_conceded INT NOT NULL,
    expected_goals_conceded REAL NOT NULL,
    shots_against INT NOT NULL,
    saves INT NOT NULL,
    penalties_saved INT NOT NULL,
    own_goals INT NOT NULL,
    yellow_cards INT NOT NULL,
    red_cards INT NOT NULL,
    bonus_points INT NOT NULL,
    bonus_points_system INT NOT NULL
);