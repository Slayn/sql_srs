# import io

import duckdb
import pandas as pd
import streamlit as st

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

solution_sql = """
SELECT * FROM data
WHERE product_name = 'redbull'
"""
solution_df = duckdb.sql(solution_sql).df()


# Titre du programme
st.write("SQL - SRS")


# Menu gauche
with st.sidebar:
    option = st.selectbox(
        "Choix du sujet à réviser :",
        ("Joins", "GroupBy", "Windows Function"),
        index=None,
        placeholder="Selection du sujet",
    )

    st.write("Sujet choisi : ", option)

# Header / toujours affiché
input_sql = st.text_area(label="Entrez votre requête :", key="user_input")

if input_sql != "":
    result = duckdb.sql(input_sql).df()

    # On force l'ordre des colonnes du résultat en fonction de la solution pour mieux gérer le compare
    try:
        result = result[solution_df.columns]
    except KeyError:
        st.write("Nombre de colonne incorrect")

    # Validation du résultat
    try:
        compare = result.compare(solution_df)
        st.write("Parfait ! C'est le bon résultat")
        st.dataframe(result)
    except:
        st.write(r"/!\ Le résultat n'est pas celui attendu")
        st.dataframe(result)


# Tab list
tab1, tab2 = st.tabs(["Tables", "Solution"])

# Tabs content
with tab1:
    st.write("Table : data")
    st.dataframe(data)
    st.write("Résultat attendu :")
    st.dataframe(solution_df)

with tab2:
    st.write(solution_sql)
