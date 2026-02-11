import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

import src.understat_scraper as us

#TODO: On one occasion, the players list was empty. Fix to ensure the scrape retries (max 3 times?) if unsuccessful.

# region Entry Point

def main():
    teams = us.get_team_names()
    print(teams)

    for team in teams:
        players = us.get_player_names_and_ids(team)
        print(f"{team}:\n{players}")

    #players = us.get_player_names_and_ids(teams[0])
    #print(players)

if __name__ == "__main__":
    main()

# endregion Entry Point