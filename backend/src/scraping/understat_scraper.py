import re
from selenium.webdriver.common.by import By

import src.scraping.scraping_handler as sh

# region Constants

YEAR = "2025" # TODO: Make this dynamic

LEAGUE_URL = "https://understat.com/league/EPL"
TEAM_URL = "https://understat.com/team/"
PLAYER_URL = "https://understat.com/player/"

# endregion Constants

# region Functions

def get_team_names():
    """
    Gets the names of the all the teams in the league; as they are in the corresponding team URLs.

    Returns:
        list[str]: The names of the teams in the league, in alphabetical order.
    """
    # Table is in the block with ID "league-chemp", and we wait until at least one row is present in the table body.
    location_conditions = [
        (By.ID, "league-chemp"),
        (By.CSS_SELECTOR, "#league-chemp tbody tr")
    ]

    teams_table = sh.selenium_scrape(
        url=LEAGUE_URL,
        locator=By.TAG_NAME,
        locator_value="table",
        wait_conditions=location_conditions
    )

    # The URL of each team is in the format "team/{team_name}/YEAR", so we extract the team name from the URL.
    pattern = re.compile(rf"team/(.*?)/{YEAR}", re.DOTALL)
    teams_list = pattern.findall(teams_table)

    # Return in alphabetical order.
    return sorted(teams_list)

def get_player_names_and_ids(team_name):
    """
    Gets all the names and corresponding IDs of the players in the specified team.

    Args:
        team_name (str): Team for which the player names and IDs are to be fetched.

    Returns:
        list[tuple[str, str, str]]: List of tuples containing the player names and IDs in the format (first_name, last_names, id).
    """

    url = f"{TEAM_URL}{team_name}/{YEAR}"

    # Table is in the block with ID "team-players", and we wait until at least one row is present in the table body.
    location_conditions = [
        (By.ID, "team-players"),
        (By.CSS_SELECTOR, "#team-players tbody tr")
    ]

    players_table = sh.selenium_scrape(
        url=url,
        locator=By.TAG_NAME,
        locator_value="table",
        wait_conditions=location_conditions
    )

    # Get just the body of the table to ignore the header row.
    pattern = re.compile(r"(<tbody>.*?</tbody>)")
    table_body = pattern.findall(players_table)[0]

    # Get each row of the table - which corresponds to a different player.
    pattern = re.compile(r"(<tr>.*?</tr>)")
    rows = pattern.findall(table_body)

    players = []
    for row in rows:
        # The URL of each player is in the format "player/{player_id}", so we extract the player ID from the URL.
        pattern = re.compile(r'<a href="player/(.*?)">')
        player_id = pattern.findall(row)[0]

        # Use the player ID to find the full name of the player.
        pattern = re.compile(rf'"player/{player_id}">(.*?)</a>')
        full_name = pattern.findall(row)[0]

        # Split the full name into first name and last name(s).
        names = full_name.split(' ')
        players += [(names[0], ' '.join(names[1:]), player_id)]

    return players

# endregion Functions







# def html_scraping():
#     page = urlopen(LEAGUE_URL)
#     html_bytes = page.read()
#     html = html_bytes.decode("utf-8")
#
#     league_index = html.find("<div id=\"league-chemp\"")
#     print(league_index)
#     print(html[league_index:])