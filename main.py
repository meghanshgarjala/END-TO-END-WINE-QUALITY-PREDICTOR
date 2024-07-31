from src.Wine_quality_prediction import logger
from Wine_quality_prediction.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME="DATA INGESTION"

try:
        logger.info(f">>>>>>STAGE {STAGE_NAME} HAS STARTED<<<<<<<<<")
        data_ingestion=DataIngestionTrainingPipeline()
        data_ingestion.main()
        logger.info(f">>>>>>STAGE {STAGE_NAME} HAS COMPLETED SUCCESSFULLY<<<<<")
        
except Exception as e:

    logger.exception(e)
    raise e
