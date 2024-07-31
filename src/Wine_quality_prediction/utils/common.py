import os
from box.exceptions import BoxValueError
import yaml
from Wine_quality_prediction import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from typing import Any
from pathlib import Path



@ensure_annotations
def read_yaml(path_to_yaml:Path)->ConfigBox:
    try:
        with open(path_to_yaml, 'r') as yamlfile:
            content = yaml.safe_load(yamlfile)
            logger.info(f"yaml_file:{path_to_yaml} loaded successfully")
        return ConfigBox(content)
    
    except BoxValueError:
        raise ValueError("yaml file is empty")
    
    except Exception as e:
        raise e
    

@ensure_annotations
def create_directories(path_to_directories:list,verbose=True):
    for path in path_to_directories:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f"Created directory at {path}")


@ensure_annotations
def save_json(path:Path,data:dict):
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)
        logger.info(f"Json file saved to {path}")


@ensure_annotations
def load_json(path:Path)->ConfigBox:
    with open(path) as f:
        content=json.laod(f)
        logger.info(f"Json file loaded successfully from {path}")
        return ConfigBox(content)
    


@ensure_annotations
def save_model(path:Path, model: Any):
    joblib.dump(value=model,filename=path)
    logger.info(f"Model saved to {path}")



@ensure_annotations
def load_model(path:Path)->Any:
    data=joblib.load(path)
    logger.info(f"Model saved to {path}")
    return data