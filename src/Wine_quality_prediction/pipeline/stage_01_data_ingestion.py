from Wine_quality_prediction import  logger
from Wine_quality_prediction.config.configuration import ConfigurationManager
from Wine_quality_prediction.components.dataingestion import DataIngestion




STAGE_NAME="DATA INGESTION STAGE"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):

        config=ConfigurationManager()

        data_ingestion_config=config.get_dataingestionconfig()

        data_ingestion=DataIngestion(data_ingestion_config)

        data_ingestion.download_data()

        data_ingestion.extract_file()

if __name__=="__main__":

    try:
        logger.info(f">>>>>>STAGE {STAGE_NAME} HAS STARTED<<<<<<<<<")
        obj=DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>STAGE {STAGE_NAME} HAS COMPLETED SUCCESSFULLY<<<<<")
        
    except Exception as e:
        logger.exception(e)
        raise e

