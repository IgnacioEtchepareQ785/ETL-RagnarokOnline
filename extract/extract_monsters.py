import requests
import time
from config.settings import BASE_URL, HEADERS

def extract_monster(monster_id):
    url = f"{BASE_URL}/{monster_id}"
    response = requests.get(url, headers=HEADERS, timeout=10)

    if response.status_code != 200 or not response.text.strip():
        return None

    try:
        return response.json()
    except Exception:
        return None


def extract_monsters(monster_ids):
    monsters = []

    for monster_id in monster_ids:
        data = extract_monster(monster_id)

        if data:
            monsters.append(data)
            print(f"✔ Monster {monster_id} extraído")
        else:
            print(f"⚠ Monster {monster_id} inválido")

        time.sleep(0.5)

    return monsters
