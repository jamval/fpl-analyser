
CREATE TABLE IF NOT EXISTS Seasons (
    season CHAR(9) PRIMARY KEY, -- E.g., 2023-2024
    season_start_date DATE NOT NULL, -- Default to 1st of August
    season_end_date DATE NOT NULL -- Default to 30th of June
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

)