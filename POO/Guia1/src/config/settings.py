import os

class Settings:
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    DATA_FILE = os.path.join(BASE_DIR, "data", "records.csv")