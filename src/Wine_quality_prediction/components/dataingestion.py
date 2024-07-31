from dataclasses import dataclass
from pathlib import Path
from Wine_quality_prediction.constants import *
from Wine_quality_prediction.utils.common import read_yaml,create_directories
from Wine_quality_prediction import  logger
import urllib.request as request
import zipfile
from Wine_quality_prediction.entity.config_entity import DataIngestionConfig
import os








class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config = config

    
    def download_data(self):
        if not os.path.exists(self.config.local_file_path):
            filename,headers=request.urlretrieve(

                url=self.config.source_URL,
                filename=self.config.local_file_path

            )

            logger.info(f"{filename} downloaded ")

        else :
            logger.info(f"{filename} not downloaded or already exists")


    def extract_file(self):
        
        unzip_filepath=self.config.unzip_dir
        os.makedirs(unzip_filepath,exist_ok=True)
        with zipfile.ZipFile(self.config.local_file_path, 'r') as zip_ref:
            zip_ref.extractall(unzip_filepath)
            logger.info(f"File extracted to {unzip_filepath}")