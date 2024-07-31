from Wine_quality_prediction.constants import *
from Wine_quality_prediction.utils.common import read_yaml,create_directories
from Wine_quality_prediction.entity.config_entity import DataIngestionConfig








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
