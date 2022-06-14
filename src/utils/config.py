"""Config values"""
from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


# Clening config
index = environ.get('INDEX_DF')
# db_user = environ.get('DATABASE_USERNAME')
# db_password = environ.get('DATABASE_PASSWORD')
# db_host = environ.get('DATABASE_HOST')
# db_port = environ.get('DATABASE_PORT')
# db_name = environ.get('DATABASE_NAME')