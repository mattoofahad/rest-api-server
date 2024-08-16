import os

from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv(), override=True)

LOGGER_LEVEL = os.getenv("LOGGER_LEVEL")
