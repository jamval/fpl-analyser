import os
from urllib.request import urlopen

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

# region Initialisation

def initialise():
    """
    Initialise the scraping handler. \n
    Checks if the datasets and dependencies directories exist, and creates them if they do not. \n
    WIP: Installs correct version of ChromeDriver if it is not already installed. \n
    Initialises Selenium webdriver options and service.
    """
    current_dir = os.getcwd()
    backend_dir = current_dir.rsplit('\\', 1)[0] + '\\'

    # Check datasets directory exists.
    data_dir = backend_dir + DATA_DIR
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

    # Check dependencies directory exists.
    dependencies_dir = backend_dir + DEPENDENCIES_DIR
    if not os.path.exists(dependencies_dir):
        os.makedirs(dependencies_dir)

    # TODO: Set up automatic install/update of ChromeDriver
    # chrome_driver_path = dependencies_dir + CHROME_DRIVER_DIR
    chrome_driver_path = "C:\\Users\\jamie\\Programming_Projects\\_dependencies\\chromedriver-win64\\"

    if not os.path.exists(chrome_driver_path):
        print("Unable to find ChromeDriver")
        return

    chrome_driver_path += CHROME_DRIVER_EXE

    # Initialise Selenium webdriver options and service.
    global _chrome_options
    _chrome_options.add_argument("--headless")
    _chrome_options.add_argument("--disable-gpu")

    global _chrome_service
    _chrome_service = ChromeService(executable_path=chrome_driver_path)

    global _initialised
    _initialised = True

# endregion Initialisation

#region Scraping Functions

def selenium_scrape(url, locator, locator_value, wait_conditions=None):
    """
    Gets the HTML of the specified element, using Selenium.

    Args:
        url (str): The URL to scrape.
        locator (str): The locator of the element that is to be returned, e.g. By.ID.
        locator_value (str): The value to locate the element that is to be returned, e.g. the ID of the element.
        wait_conditions (list[tuple[str, str]]): The locator condition-value pairs to wait for before the element is returned, e.g. (By.ID, "element_id"). The wait conditions are performed in order of index.

    Returns:
        str: The HTML of the specified element.
    """
    if not _initialised:
        print("Scraping handler not yet initialised")
        return ""

    driver = webdriver.Chrome(service=_chrome_service, options=_chrome_options)
    driver.get(url)
    try:
        wait = WebDriverWait(driver, 10)

        if wait_conditions is not None:
            element = wait.until(EC.presence_of_element_located(wait_conditions[0]))
            for i in range(len(wait_conditions) - 1):
                wait.until(EC.presence_of_element_located(wait_conditions[i + 1]))

            element = element.find_element(locator, locator_value)
        else:
            element = wait.until(EC.presence_of_element_located((locator, locator_value)))

        return element.get_attribute("outerHTML")
    except Exception as e:
        print(e)
    finally:
        driver.quit()

def html_scrape(url):
    """
    Returns the HTML of the entire webpage located at the specified URL.

    Args:
        url (str): The URL to scrape.

    Returns:
        str: The HTML of the webpage.
    """
    if not _initialised:
        print("Scraping handler not yet initialised")
        return ""

    page = urlopen(url)
    html_bytes = page.read()
    return html_bytes.decode("utf-8")

# endregion Scraping Functions