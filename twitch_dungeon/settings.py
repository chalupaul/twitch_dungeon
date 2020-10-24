# settings.py
import os
from dotenv import load_dotenv

load_dotenv(verbose=True)

config = {"DATABASE_URL": os.environ["DB_URL"]}
