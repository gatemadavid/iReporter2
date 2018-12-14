import os


class Config(object):
    """Parent configuration class."""
    DEBUG = False
    CSRF_ENABLED = True
    URL = os.getenv('DATABASE_URL')


class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = True


class TestingConfig(Config):

    TESTING = True
    DEBUG = True
    URL = os.getenv('DATABASE_TEST_URL')


class ProductionConfig(Config):
    """Configurations for Production."""
    DEBUG = False
    TESTING = False


app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
}
