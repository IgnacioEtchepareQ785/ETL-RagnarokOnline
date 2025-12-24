from extract.extract_monsters import extract_monsters
from transform.transform_drops import transform_drops
from load.load_to_postgres  import load_to_postgres
from config.settings import MONSTER_IDS, OUTPUT_PATH
# from load.load_to_csv import load_to_csv

def main():
    monsters = extract_monsters(MONSTER_IDS)
    rows = transform_drops(monsters)
    # load_to_csv(rows, OUTPUT_PATH)
    load_to_postgres(rows)
    

if __name__ == "__main__":
    main()
