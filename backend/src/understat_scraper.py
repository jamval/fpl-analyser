import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
import re

from selenium.webdriver.common.by import By

import scraping_handler as sh

import json
import requests

# region Constants

LEAGUE_URL = "https://understat.com/league/EPL"
TEAM_URL = "https://understat.com/team/"
PLAYER_URL = "https://understat.com/player/"

# endregion Constants

# region Functions

def get_team_names():
    """
    Gets the names of the all the teams in the league, as they are in the corresponding team URLs.

    Returns:
        list[str]: The names of the teams in the league, in alphabetical order.
    """
    # Table is in the "league-chemp" block, and we wait until at least one row is present in the table body.
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

    # The URL of each team is in the format "team/{team_name}/2025", so we extract the team name from the URL.
    pattern = re.compile(r"team/(.*?)/2025", re.DOTALL)
    teams_list = pattern.findall(teams_table)

    # Return in alphabetical order.
    return sorted(teams_list)

# endregion Functions






# def selenium_scraping():
#     driver = webdriver.Chrome(service=service, options=chrome_options)
#     driver.get(LEAGUE_URL)
#     try:
#         wait = WebDriverWait(driver, 10)
#         table = wait.until(EC.presence_of_element_located((By.ID, "league-chemp")))
#         # Wait for at least one data row
#         wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#league-chemp tbody tr")))
#
#         table = table.find_element(By.TAG_NAME, "table")
#         html_table = table.get_attribute("outerHTML")
#         print(html_table)
#
#         #TODO: similar thing for each cell in row
#         pattern = re.compile(r"(<tr>.*?</tr>)", re.DOTALL)
#         rows = pattern.findall(html_table)
#
#         for row in rows[1:]:
#             pattern = re.compile(r"(<td.*?</td>)", re.DOTALL)
#             cells = pattern.findall(row)
#             print(cells)
#             #TODO: Sort out
#             # Team name
#             pattern = re.compile(r'2025">(.*?)</a>')
#             print(pattern.findall(cells[1]))
#
#
#         #print(matches)
#         #teams_list = []
#         #name_index = html_table.find("<a href=")
#
#         #while name_index != -1:
#         #    html_table = html_table[name_index + len("<a href="):]
#
#         # print(html_table.find("<a href="))
#         # print(html_table[1019:1119])
#     except Exception as e:
#         print(e)
#     finally:
#         driver.quit()
#
# def html_scraping():
#     page = urlopen(LEAGUE_URL)
#     html_bytes = page.read()
#     html = html_bytes.decode("utf-8")
#
#     league_index = html.find("<div id=\"league-chemp\"")
#     print(league_index)
#     print(html[league_index:])