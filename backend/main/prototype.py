import sys
import os
backend_dir_index = __file__.find("\\backend\\")
sys.path.append(os.path.join(__file__[:backend_dir_index + len("\\backend\\")], "src"))

import src.scraping.understat_scraper as us

#TODO: On one occasion, the players list was empty. Fix to ensure the scrape retries (max 3 times?) if unsuccessful.

# region Entry Point

def main():
    teams = us.get_team_names()
    print(teams)

    for team in teams:
        players = us.get_player_names_and_ids(team)
        print(f"{team}:\n{players}")

    pass

if __name__ == "__main__":
    main()

# endregion Entry Point