import os
from pathlib import Path
import logging as lg
lg.basicConfig(level=lg.INFO, format='[%(asctime)s]: %(name)s - %(levelname)s - %(message)s'    )
list_of_files = [
    "src/__init__.py",
    "src/helper.py",
    "src/prompt.py",
    ".env",
    "requirement.txt",
    "setup.py",
    "research/trials.ipynb",
    "app.py"
]


for filepath in list_of_files:
    filepath=Path(filepath)
    filedir, filename = os.path.split(filepath)
    print(filedir)
    print(filename)
    if filedir!="":
        os.makedirs(filedir,exist_ok=True)
        lg.info(f"Creating directory: {filedir} for the file: {filename}")
    if(not os.path.exists(filepath) or(os.path.getsize(filepath))==0):
        with open(filepath,'w') as f:
            pass
            lg.info(f"creating empty file:{filepath} ")
    else:
        lg.info(f"{filename} is already exists")