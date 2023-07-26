from CnnClassifier import logger
from CnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from CnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelPipeline
STAGE_NAME = "Data Ingestion Stage"
try:
        logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
        data_ingestion = DataIngestionTrainingPipeline()
        data_ingestion.main()
        logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<\n\rx=======================x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Prepare Base Model"
try:
        logger.info(f"********************************")
        logger.info(f"<<<<<<<<<<<< Starting {STAGE_NAME} started <<<<<<<<<<<<")
        obj = PrepareBaseModelPipeline()
        obj.main()
        logger.info(f"<<<<<<<<<<<< {STAGE_NAME} completed <<<<<<<<<<<<\n\rx===========================x")
except Exception as e:
        logger.exception(e)
        raise e