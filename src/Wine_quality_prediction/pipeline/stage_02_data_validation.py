from Wine_quality_prediction import  logger
from Wine_quality_prediction.config.configuration import ConfigurationManager
from Wine_quality_prediction.components.datavalidation import DataValiadtion




STAGE_NAME="DATA VALIDATION STAGE"

class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):

        config = ConfigurationManager()

        data_validation_config = config.get_data_validation_config()

        data_validation = DataValiadtion(config=data_validation_config)

        data_validation.validate_all_columns()
if __name__=="__main__":

    try:
        logger.info(f">>>>>>STAGE {STAGE_NAME} HAS STARTED<<<<<<<<<")
        obj=DataValidationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>STAGE {STAGE_NAME} HAS COMPLETED SUCCESSFULLY<<<<<")
        
    except Exception as e:
        logger.exception(e)
        raise e

