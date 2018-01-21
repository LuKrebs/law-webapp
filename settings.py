import os

SECRET_KEY = "1234"
DEBUG = True

DB_USERNAME = 'app_user'
DB_PASSWORD = 'app_password'
BLOG_DATABASE_NAME = 'laracunha_db'
DB_HOST = os.getenv('IP', '0.0.0.0.')

DB_URI = "mysql+pymysql://{}:{}@{}/{}".format(DB_USERNAME, DB_PASSWORD,DB_HOST,BLOG_DATABASE_NAME)
SQLALCHEMY_DATABASE_URI = DB_URI

SQLALCHEMY_TRACK_MODIFICATIONS = True

UPLOADED_IMAGES_DEST = "/home/luciano/code/projects/laracunha/static/images"
UPLOADED_IMAGES_URL = "/static/images/"
