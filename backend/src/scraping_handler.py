import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# region Constants

DATA_DIR = "datasets\\"
DEPENDENCIES_DIR = "dependencies\\"
CHROME_DRIVER_DIR = "chromedriver-win64\\"
CHROME_DRIVER_EXE = "chromedriver.exe"

# endregion Constants

# region Variables

_initialised = False
_chrome_options = Options()
_chrome_service = ChromeService()

# endregion Variables

# region Functions

def initialise():
    """
    Initialise the scraping handler.
    """
    current_dir = os.getcwd()
    backend_dir = current_dir.rsplit('\\', 1)[0] + '\\'

    # Check data directory exists.
    data_dir = backend_dir + DATA_DIR
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

    # Check dependencies directory exists.
    dependencies_dir = backend_dir + DEPENDENCIES_DIR
    if not os.path.exists(dependencies_dir):
        os.makedirs(dependencies_dir)

    # Initialise Selenium.
    # TODO: Set up automatic install/update of ChromeDriver
    # chrome_driver_path = dependencies_dir + CHROME_DRIVER_DIR
    chrome_driver_path = "C:\\Users\\jamie\\Programming_Projects\\_dependencies\\chromedriver-win64\\"

    if not os.path.exists(chrome_driver_path):
        print("Unable to find ChromeDriver")
        return

    chrome_driver_path += CHROME_DRIVER_EXE

    global _chrome_options
    _chrome_options.add_argument("--headless")
    _chrome_options.add_argument("--disable-gpu")

    global _chrome_service
    _chrome_service = ChromeService(executable_path=chrome_driver_path)

    global _initialised
    _initialised = True

# endregion Functions