import os
import pathlib
from pathlib import Path        # this is used to create the path on the basis of our OS(windows, Linux, Mac)
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s: ')

package_name = 'deepClassifier'

# Writing the code of Our basic default file folder structure

# Here in the SRC folder all the python code file will be there .
list_of_files = [
    ".github/workflows/.gitkeep",               # This is used when there is empty folder and we want to upload in github at that time this .gitkeep file is created in the empty folder to maintain the structure n upload it on the github...
    f"src/{package_name}/__init__.py",          # __init__.py this will help to understand that this is package.
    f"src/{package_name}/components/__init__.py",
    f"src/{package_name}/utils/__init__.py",
    f"src/{package_name}/config/__init__.py",
    f"src/{package_name}/pipeline/__init__.py",
    f"src/{package_name}/entity/__init__.py",
    f"src/{package_name}/constants/__init__.py",
    "tests/__init__.py",
    "tests/unit/__init__.py",               # Unit test is uded for testing the unit means single (specific class).
    "tests/integration/__init__.py",        # Integration test is used for testing the two component together.
    "configs/config.yaml",                  # all the configuration will be there in this file.
    "dvc.yaml",                             # this is used to create the Data Version Control Pipeline.
    "params.yaml",                          # in this all the training parameters will be there on one place.
    "init_setup.sh",                        # this is shell script file which will help us to create the environment.
    "requirements.txt",                      # this is the file in which all the requirements are there to run the project.
    "requirements_dev.txt",                  # this is the file in which all the requirements are there to for the developemet purpose.
    "setup.py",                             # this files have all the setup details.
    "setup.cfg",                            # this is used to create the packages.
    "pyproject.toml",                       # this is used to create the packages.
    "tox.ini",                              # this is used to do testing of the porject locally.
    "research/trials.ipynb"                 # this is used to do testing in trial section.
]

# Code for checking and creating the Directory and Files...

for filepath in list_of_files:   # Create a forloop.
    filepath = Path(filepath)    # Creating the perfect filepath.
    filedir, filename = os.path.split(filepath)
    print(filedir, filename)
    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f'Creating directory: {filedir} for file: {filename}')
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass # Creating the empty file
            logging.info(f"Creating empty file: {filedir}")
    else:
        logging.info(f"{filename} already exist...")