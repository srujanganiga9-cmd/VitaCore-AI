import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATASET_PATH = os.path.join(BASE_DIR, "dataset", "nutrition.csv")

df = pd.read_csv(DATASET_PATH)
print(df.columns.tolist())

df = df.fillna("")


def search_food(query):

    query = query.lower()

    matches = df[
        df["food_name"].str.lower().str.contains(query)
    ]

    return matches.head(8)["food_name"].tolist()


def get_food(food_name):
    
    print("Received:", repr(food_name))

    print(df["food_name"].head(10).tolist())

    result = df[
        df["food_name"].astype(str).str.strip().str.lower()
        == food_name.strip().lower()
    ]

    print("Matches:", len(result))

    if result.empty:
        return None

    return result.iloc[0].to_dict()