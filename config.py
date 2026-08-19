import os
from dotenv import load_dotenv

# Load once here
load_dotenv()

# Fetch variables
KAGGLE_URL = os.getenv("KAGGLE_URL")