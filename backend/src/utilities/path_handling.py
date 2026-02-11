import os

# region Constants

CONFIG_DIR = "config\\"
DATA_DIR = "datasets\\"
DEPENDENCIES_DIR = "dependencies\\"
CHROME_DRIVER_DIR = "chromedriver-win64\\"
CHROME_DRIVER_EXE = "chromedriver.exe"

# endregion Constants

# region Functions

def backend_path():
    """
    Gets the file path of the backend directory including the backend directory name. \n
    E.g., "C:\\Users\\...\\fpl-analyser\\backend\\".

    Returns:
        str: The file path of the backend directory including the backend directory name.
    """
    current_dir = os.getcwd()
    backend_dir_index = current_dir.find("\\backend\\")
    return current_dir[:backend_dir_index + len("\\backend\\")]

# endregion Functions