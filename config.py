import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET-KEY') or 'never-guess'

DB_FILE_PATH = os.getcwd()+'/db/database.xml'