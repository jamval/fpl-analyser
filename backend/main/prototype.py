import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

import src.understat_scraper as us

# region Entry Point

def main():
    print(us.get_team_names())

if __name__ == "__main__":
    main()

# endregion Entry Point