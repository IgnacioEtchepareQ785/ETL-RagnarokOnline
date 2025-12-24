import pandas as pd
from sqlalchemy import create_engine
from config.settings import DB_CONFIG

def load_to_postgres(rows):
    df = pd.DataFrame(rows)

    engine = create_engine(
        f"postgresql+psycopg2://{DB_CONFIG['user']}:{DB_CONFIG['password']}"
        f"@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}"
    )

    df.to_sql(
        "monster_drops",
        engine,
        if_exists="append",
        index=False
    )

    print("✅ Datos cargados en PostgreSQL")
