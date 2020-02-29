import logging
import logging.config
from app.config import ConfigLoader, AppConfig, LoggingConfig


class LoggerBuilder:
    def __init__(self):
        config: AppConfig = ConfigLoader.load()
        # self._config: LoggingConfig = py_api_template_config.logging_config
        self._config: LoggingConfig = config.logging_config

    def get_logger(self, logger_name: str) -> logging.Logger:
        logger = logging.getLogger(logger_name)
        handler = logging.StreamHandler()
        formatter = logging.Formatter(self._config.format)
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(self._config.level)
        return logger
