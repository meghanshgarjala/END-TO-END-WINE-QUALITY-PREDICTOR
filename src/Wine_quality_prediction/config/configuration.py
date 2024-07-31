from Wine_quality_prediction.constants import *
from Wine_quality_prediction.utils.common import read_yaml,create_directories
from Wine_quality_prediction.entity.config_entity import DataIngestionConfig,DataValidationConfig








class ConfigurationManager:
    def __init__(
            self,
            config_filepath=CONFIG_FILE_PATH,
            params_filepath=PARAMS_FILE_PATH,
            schema_filepath=SCHEMA_FILE_PATH
             ):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)

        create_directories([self.config.artifacts_root])




    def get_dataingestionconfig(self)->DataIngestionConfig:
        config=self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=Path(config.root_dir),
            source_URL=config.source_URL,
            local_file_path=Path(config.local_file_path),
            unzip_dir=Path(config.unzip_dir)
        )

        return data_ingestion_config
    
     
    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation
        schema = self.schema.COLUMNS

        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir=config.root_dir,
            STATUS_FILE=config.STATUS_FILE,
            dataset_path = config.dataset_path,
            all_schema=schema,
        )

        return data_validation_config
