import os
from dotenv import load_dotenv

load_dotenv()
DEBUG = False

PREFIX = ["!"]
VERSION = "1"

TOKEN = os.getenv("TOKEN")

# Canvas API
CANVAS_URL = os.getenv("CANVAS_URL")
CANVAS_KEY = os.getenv("CANVAS_KEY")

# Clv's DB API