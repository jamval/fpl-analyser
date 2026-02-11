import json
import os
import requests
from urllib.request import urlopen
import re

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pandas as pd

# Setup for Selenium
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
# TODO
service = ChromeService(executable_path=r"C:\Users\jamie\Programming_Projects\_dependencies\chromedriver-win64\chromedriver.exe")

# region Constants

DATA_DIR = "data/"

LEAGUE_URL = "https://understat.com/league/EPL"
TEAM_URL = "https://understat.com/team/"
PLAYER_URL = "https://understat.com/player/"

# endregion Constants

# region Entry Point

def main():
    current_dir = os.getcwd()
    data_dir = current_dir.rsplit('\\', 1)[0] + "data/"
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

    selenium_scraping()
    #html_scraping()

# region Entry Point

# region Functions

def selenium_scraping():
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get(LEAGUE_URL)
    try:
        wait = WebDriverWait(driver, 10)
        table = wait.until(EC.presence_of_element_located((By.ID, "league-chemp")))
        # Wait for at least one data row
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#league-chemp tbody tr")))

        table = table.find_element(By.TAG_NAME, "table")
        html_table = table.get_attribute("outerHTML")

        #TODO: similar thing for each cell in row
        pattern = re.compile(r"(<tr>.*?</tr>)", re.DOTALL)
        rows = pattern.findall(html_table)

        for row in rows[1:]:
            pattern = re.compile(r"(<td.*?</td>)", re.DOTALL)
            cells = pattern.findall(row)
            print(cells)
            #TODO: Sort out
            # Team name
            pattern = re.compile(r'2025">(.*?)</a>')
            print(pattern.findall(cells[1]))


        #print(matches)
        teams_list = []
        #name_index = html_table.find("<a href=")

        #while name_index != -1:
        #    html_table = html_table[name_index + len("<a href="):]

        print(html_table.find("<a href="))
        print(html_table[1019:1119])
    except Exception as e:
        print(e)
    finally:
        driver.quit()

def html_scraping():
    page = urlopen(LEAGUE_URL)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")

    league_index = html.find("<div id=\"league-chemp\"")
    print(league_index)
    print(html[league_index:])

def get_teams():

    pass

# region Functions

if __name__ == "__main__":
    main()