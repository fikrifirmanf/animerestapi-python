import os


BASE_URL = os.environ.get("BASE_URL","https://otakudesu.watch/")
APP_MODE = os.environ.get("APP_MODE","development")
ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "localhost,127.0.0.1").split(",")