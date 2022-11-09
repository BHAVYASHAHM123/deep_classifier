from deepClassifier.config import ConfigurationManager
from deepClassifier.components import PrepareBaseModel
from deepClassifier import logger

STAGE_NAME = "Prepare base model"

def main():
    config = ConfigurationManager()
    prepareBaseModel_config = config.get_prepare_base_model_config()
    prepareBaseModel = PrepareBaseModel(config=prepareBaseModel_config)
    prepareBaseModel.get_base_model()
    prepareBaseModel.update_base_model()

if __name__ == '__main__':
    try:
        logger.info(f"**********************************************")
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e