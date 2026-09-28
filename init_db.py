import io

import duckdb
import pandas as pd

# Connexion à la base duckdb
con = duckdb.connect(database="data/exercices_sql_tables.duckdb", read_only=False)


# --------------------------------------------------------------------
# LIST DES EXOS
# --------------------------------------------------------------------
data = {
    "theme": ["cross_joins", "window_functions"],
    "exercise_name": ["beverages_and_food", "simple_window"],
    "tables": [["beverages", "food_items"], "simple_window"],
    "last_reviewed": ["1970-01-01", "1970-01-01"],
}
memory_state_df = pd.DataFrame(data)
con.execute("CREATE TABLE IF NOT EXISTS memory_state AS SELECT * FROM memory_state_df")


# ------------------------------------------------------------
# CROSS JOIN EXERCISES
# ------------------------------------------------------------
csv = """
beverage,price
orange juice,2.5
Expresso,2
Tea,3
"""
beverages = pd.read_csv(io.StringIO(csv))
con.execute("CREATE TABLE IF NOT EXISTS beverages AS SELECT * FROM beverages")

csv2 = """
food_item,food_price
cookie juice,2.5
chocolatine,2
muffin,3
"""
food_items = pd.read_csv(io.StringIO(csv2))
con.execute("CREATE TABLE IF NOT EXISTS food_items AS SELECT * FROM food_items")


# --------------------------------------------------------------------
# Données perso fictives
# --------------------------------------------------------------------
# Gestion des données
data = {
    "store_id": [
        "Armentieres",
        "Armentieres",
        "Armentieres",
        "Armentieres",
        "Lille",
        "Lille",
        "Lille",
        "Lille",
        "Douai",
        "Douai",
        "Douai",
        "Douai",
    ],
    "product_name": [
        "redbull",
        "chips",
        "wine",
        "redbull",
        "redbull",
        "chips",
        "wine",
        "icecream",
        "redbull",
        "chips",
        "wine",
        "icecream",
    ],
    "amount": [45, 60, 60, 45, 100, 140, 190, 170, 55, 70, 20, 45],
}
data = pd.DataFrame(data)
con.execute("CREATE TABLE IF NOT EXISTS data AS SELECT * FROM data")
