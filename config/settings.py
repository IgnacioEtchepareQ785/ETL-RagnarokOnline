# config/settings.py

BASE_URL = "https://ragnapi.com/api/v1/old-times/monsters"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Ragnarok-ETL)"
}

MONSTER_IDS = [1001, 1002, 1003, 1004, 1005]

OUTPUT_PATH = "data/monster_drops.csv"

DB_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "database": "ragnarok",
    "user": "postgres",
    "password": "nacho1313"
}
