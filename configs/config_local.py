from config import *
import os

DEFAULT_SERVER = '0.0.0.0'
DEFAULT_SERVER_PORT = int(os.getenv('DEFAULT_SERVER_PORT', '5050'))

SECRET_KEY = '{{=randomString(32)}}'
CSRF_SESSION_KEY = '{{=randomString(32)}}'
SECURITY_PASSWORD_SALT = '{{=randomString(32)}}'
