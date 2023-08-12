import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s:')

projectName='textSummarizer'

listOfFiles=[
    ".github/workflows/.gitkeep",
    f'src/{projectName}/__init__.py',
    f'src/{projectName}/components/__init__.py',
    f'src/{projectName}/utils/__init__.py',
    f'src/{projectName}/utils/common.py',
    f'src/{projectName}/logging/__init__.py',
    f'src/{projectName}/config/__init__.py',
    f'src/{projectName}/config/configurations.py',
    f'src/{projectName}/pipeline/__init__.py',
    f'src/{projectName}/entity/__init__.py',
    f'src/{projectName}/constants/__init__.py',
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "test.py",
]

for filePath in listOfFiles:
    filePath=Path(filePath)

    fileDir,filename=os.path.split(filePath)

    if fileDir!='':
        os.makedirs(fileDir,exist_ok=True)
        logging.info(f"Creating directory: {fileDir} for the file {filename}")
    
    if((not os.path.exists(filePath)) or os.path.getsize(filePath)!=0):
        
        with open(filePath,'w') as file:
            pass
            logging.info(f'Creating empty file {filePath}')
    else:
        logging.info(f'{filename} already exists')
