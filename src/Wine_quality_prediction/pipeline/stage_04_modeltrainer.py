from  Wine_quality_prediction.config.configuration import ConfigurationManager
from Wine_quality_prediction import logger
from Wine_quality_prediction.components.modeltrainer import ModelTrainer

STAGE_NAME = "Model Trainer stage"

class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer_config = ModelTrainer(config=model_trainer_config)
        model_trainer_config.train()




if __name__ == '__main__':

    try:
        logger.info(f">>>>>> STAGE {STAGE_NAME} HAS STARTED <<<<<<")
        obj = ModelTrainerTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> STAGE {STAGE_NAME} HAS COMPLETED <<<<<<")

    except Exception as e:
        logger.exception(e)
        raise e