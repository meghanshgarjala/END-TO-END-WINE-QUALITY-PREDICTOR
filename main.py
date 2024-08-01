from src.Wine_quality_prediction import logger
from Wine_quality_prediction.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from Wine_quality_prediction.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from Wine_quality_prediction.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from Wine_quality_prediction.pipeline.stage_04_modeltrainer import ModelTrainerTrainingPipeline
from Wine_quality_prediction.pipeline.stage_05_modelevaluation import ModelEvaluationTrainingPipeline

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
        data_validation = DataValidationTrainingPipeline()
        data_validation.main()
        logger.info(f">>>>>> STAGE {STAGE_NAME} HAS CO<PLETED SUCCESSFULLY <<<<<<")

except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME = "DATA TRANSFORMATION STAGE"
try:
   
   logger.info(f">>>>>> STAGE {STAGE_NAME} HAS STARTED <<<<<<") 
   data_transformation = DataTransformationTrainingPipeline()
   data_transformation.main()
   logger.info(f">>>>>> STAGE {STAGE_NAME} COMPLETED <<<<<<")

except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME = "MODEL TRAINER STAGE"
try:
   logger.info(f">>>>>> STAGE {STAGE_NAME} HAS STARTED <<<<<<") 
   model_trainer = ModelTrainerTrainingPipeline()
   model_trainer.main()
   logger.info(f">>>>>> STAGE {STAGE_NAME} HAS COMPLETED <<<<<<")
except Exception as e:
        logger.exception(e)
        raise e



STAGE_NAME = "MODEL EVALUATION STAGE"
try:
   logger.info(f">>>>>> STAGE {STAGE_NAME} HAS STARTED <<<<<<") 
   model_evaluation = ModelEvaluationTrainingPipeline()
   model_evaluation.main()
   logger.info(f">>>>>> STAGE {STAGE_NAME} HAS COMPLETED <<<<<<")
except Exception as e:
        logger.exception(e)
        raise e

