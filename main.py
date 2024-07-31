from src.Wine_quality_prediction import logger
from Wine_quality_prediction.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from Wine_quality_prediction.pipeline.stage_02_data_validation import DataValidationTrainingPipeline



STAGE_NAME="DATA INGESTION"

try:
        logger.info(f">>>>>>STAGE {STAGE_NAME} HAS STARTED<<<<<<<<<")
        data_ingestion=DataIngestionTrainingPipeline()
        data_ingestion.main()
        logger.info(f">>>>>>STAGE {STAGE_NAME} HAS COMPLETED SUCCESSFULLY<<<<<")
        
except Exception as e:

    logger.exception(e)
    raise e



STAGE_NAME = "DATA VALIDATION"
try:
        logger.info(f">>>>>> STAGE {STAGE_NAME} HAS STARTED <<<<<<") 
        data_ingestion = DataValidationTrainingPipeline()
        data_ingestion.main()
        logger.info(f">>>>>> STAGE {STAGE_NAME} HAS CO<PLETED SUCCESSFULLY <<<<<<")

except Exception as e:
        logger.exception(e)
        raise e