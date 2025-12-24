def transform_drops(monsters):
    rows = []

    for monster in monsters:
        for drop in monster.get("drops", []):
            rows.append({
                "monster_id": monster.get("monster_id"),
                "monster_name": monster.get("monster_info"),
                "item_name": drop.get("name"),
                "drop_rate": drop.get("rate")
            })

    return rows
