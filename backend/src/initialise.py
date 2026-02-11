import os
from src.utilities.path_handling import backend_path, CONFIG_DIR, DATA_DIR, DEPENDENCIES_DIR, CHROME_DRIVER_DIR
import config_handler as conf

# region Variables

chrome_driver_filename = ""

# endregion Variables

# region Main

def initialise():
    initialise_directories()
    pass

# endregion Main

# region Functions

def initialise_directories():
    """



    """
    directories = [CONFIG_DIR, DATA_DIR, DEPENDENCIES_DIR]

    for directory in directories:
        directory_path = os.path.join(backend_path(), directory)
        if not os.path.exists(directory_path):
            os.makedirs(directory_path)

def initialise_config():
    config_path = os.path.join(backend_path(), CONFIG_DIR)

def initialise_chrome_driver():
    driver_directory_path = os.path.join(backend_path(), DEPENDENCIES_DIR, CHROME_DRIVER_DIR)

# endregion Functions