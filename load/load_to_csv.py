import pandas as pd
import os

def load_to_csv(rows, output_path):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    df = pd.DataFrame(rows)
    df.to_csv(output_path, index=False)

    print(f"📁 Datos guardados en {output_path}")
