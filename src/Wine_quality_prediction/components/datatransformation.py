from Wine_quality_prediction.entity.config_entity import DataTransformationConfig
from sklearn.model_selection import train_test_split
import pandas as pd
from Wine_quality_prediction import logger
import os




class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    def train_test_split(self):

        data=pd.read_csv(self.config.dataset_path)

        train, test = train_test_split(data, test_size=0.2, random_state=42)

        train.to_csv(os.path.join(self.config.root_dir,"train.csv"), index=False)
        
        test.to_csv(os.path.join(self.config.root_dir,"test.csv"), index=False)

        logger.info("TRAIN TEST SPLIT DONE")

        logger.info(train.shape)

        logger.info(test.shape)