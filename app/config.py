from configparser import ConfigParser, InterpolationDepthError
import configparser
import os


class LoggingConfig:

    def __init__(self, logging_level: str, format: str):
        self._level = logging_level
        self._format = format

    @property
    def level(self):
        return self._level

    @property
    def format(self):
        return self._format


class AwsConfig:
    def __init__(self, aws_access_key_id: str, aws_secret_access_key: str):
        self._aws_access_key_id = aws_access_key_id
        self._aws_secret_access_key = aws_secret_access_key

    @property
    def aws_acces_key_id(self):
        return self._aws_access_key_id

    @property
    def aws_secret_access_key(self):
        return self._aws_secret_access_key


class AppConfig:

    def __init__(self, logging_config: LoggingConfig, aws_config: AwsConfig):
        self._logging_config = logging_config
        self._aws_config = aws_config

    @property
    def logging_config(self):
        return self._logging_config

    @property
    def aws_config(self):
        return self._aws_config


class EnvInterpolation(configparser.BasicInterpolation):
    """Interpolation which expands environment variables in values."""

    def before_get(self, parser, section, option, value, defaults):
        return os.path.expandvars(value)


class ConfigLoader:
    allowed_envs = ['local', 'production']

    @staticmethod
    def _get_file_path():
        config_directory = '/app/config'
        env = os.getenv('ENV')

        if not config_directory:
            raise Exception('Environment variable CONFIG_DIRECTORY not set')

        if not env:
            raise Exception('Environment variable ENV not set')
        elif env.lower() not in ConfigLoader.allowed_envs:
            raise Exception(f"Unknown environment {env}. It should be one of {', '.join(ConfigLoader.allowed_envs)}")
        else:
            return '{config_directory}/{env}.ini'.format(
                config_directory=config_directory.lower(),
                env=env.lower()
            )

    @staticmethod
    def get_config_value(config, section, option, default_value=None):
        try:
            return config.get(section=section, option=option)
        except:
            return default_value

    @staticmethod
    def parse_config():
        parser: ConfigParser = ConfigParser(os.environ, interpolation=EnvInterpolation())
        config_path = ConfigLoader._get_file_path()
        parser.read(config_path)
        return parser

    @staticmethod
    def load():
        config: ConfigParser = ConfigLoader.parse_config()
        try:
            logging_config = LoggingConfig(
                logging_level=config.get('LOGGING', 'logging_level'),
                format=config.get('LOGGING', 'format')
            )
            aws_config = AwsConfig(
                aws_access_key_id=config.get('AWS', 'aws_access_key_id'),
                aws_secret_access_key=config.get('AWS', 'aws_secret_access_key')
            )
            return AppConfig(logging_config=logging_config, aws_config=aws_config)
        except InterpolationDepthError as e:
            keys = os.environ.keys()
            raise Exception(f'Error while interpolating environment variables: {e}. Available variables: '
                            f'{",".join(keys)}')
