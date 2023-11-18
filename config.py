import os
import logging
from os import getenv
from os import environ

class Config(object):
      API_HASH = getenv("API_HASH", "5264bf4663e9159565603522f58d3c18")
      API_ID = int(getenv("API_ID", 11973721))
      BOT_TOKEN = getenv("BOT_TOKEN", "6078234170:AAGX4CDjIN2owsTeYTFOzk47XACzFO1nZSA")
DB_URL = environ.get('DATABASE_URI', "mongodb+srv://KarthikMovies:KarthikUK007@cluster0.4l5byki.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = environ.get('DATABASE_NAME', "Cluster0")
ADMINS = int(os.environ.get("ADMINS", "1391556668"))
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001821439025"))
AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "1391556668").split())
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS", "-1001296894100")).split()))
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001589399161"))
