from app.config import ConfigLoader


class AwsBuilder:
    def __init__(self):
        config: AppConfig = ConfigLoader.load()
        self._config: config.AwsConfig = config.aws_config

    def get_credentials(self):
        return self._config.aws_acces_key_id, self._config.aws_secret_access_key
