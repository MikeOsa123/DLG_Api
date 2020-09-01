import os

# root directory of the application
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    """Default Config. Use this for development environments."""
    SECRET_KEY = os.environ.get('TEST_SECRET_KEY') or 'random-key-string'
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['m.osamwonyi@gmail.com']

class TestingConfig(Config):
    """Configurations used for Testing."""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'this-means-nothing'
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'test.db')

class ProductionConfig(Config):
    """Configurations to be used in Production."""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'Who-let-the-dogs-out?'
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'prod.db')