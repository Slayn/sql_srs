import duckdb
import pandas as pd
import streamlit as st
import io

data = {
    'store_id': ["Armentieres", "Armentieres", "Armentieres", "Armentieres", "Lille", "Lille", "Lille", "Lille", "Douai", "Douai", "Douai", "Douai"],
    'product_name': ['redbull', 'chips', 'wine', 'redbull', 'redbull', 'chips', 'wine', 'icecream', 'redbull', 'chips', 'wine', 'icecream'],
    'amount': [45, 60, 60, 45, 100, 140, 190, 170, 55, 70, 20, 45]
}
data = pd.DataFrame(data)

answer = """
SELECT * FROM data
WHERE product_name = 'redbull'
"""

solution = duckdb.sql(answer).df()


# Titre
st.write("SQL - SRS")


# Menu gauche
with st.sidebar:
    option = st.selectbox(
        "Choix du sujet à réviser :",
        ("Joins", "GroupBy", "Windows Function"),
        index=None,
        placeholder="Selection du sujet"
    )

    st.write('Sujet choisi : ', option)


# Header / toujours affiché


input_sql = st.text_area(label="Entrez votre requête :", key="user_input")

if input_sql != '':
    resutlat_sql = duckdb.sql(input_sql).df()
    st.dataframe(resutlat_sql)


# Tab list
tab1, tab2 = st.tabs(["Tables", "Solution"])

# Content
with tab1:
    st.write('Table : data')
    st.dataframe(data)
    st.write('Résultat attendu :')
    st.dataframe(solution)

with tab2:
    st.write(answer)