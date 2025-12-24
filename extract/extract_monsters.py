import requests
import time
from config.settings import BASE_URL, HEADERS
from utils.logger import logger


def extract_monster(monster_id):
    url = f"{BASE_URL}/{monster_id}"
    response = requests.get(url, headers=HEADERS, timeout=10)

    if response.status_code != 200 or not response.text.strip():
        logger.warning(f"Monster {monster_id} no existe o respuesta inválida")
        return None

    try:
        return response.json()
    except Exception as e:
        logger.error(f"Error JSON en monster {monster_id}: {e}")
        return None


def extract_monsters(monster_ids):
    monsters = []

    for monster_id in monster_ids:
        data = extract_monster(monster_id)

        if data:
            monsters.append(data)
            logger.info(f"Monster {monster_id} extraído correctamente")
        else:
            logger.warning(f"Monster {monster_id} omitido")

        time.sleep(0.5)

    return monsters
