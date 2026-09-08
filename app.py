import duckdb
import pandas as pd
import streamlit as st

st.write("SQL - SRS")

option = st.selectbox(
    "Choix du sujet à réviser :",
    ("Joins", "GroupBy", "Windows Function"),
    index=None,
    placeholder="Selection du sujet"
)

st.write('Sujet choisi : ', option)

tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Howl"])

data = {
    'store_id': ["Armentieres", "Armentieres", "Armentieres", "Armentieres", "Lille", "Lille", "Lille", "Lille", "Douai", "Douai", "Douai", "Douai"],
    'product_name': ['redbull', 'chips', 'wine', 'redbull', 'redbull', 'chips', 'wine', 'icecream', 'redbull', 'chips', 'wine', 'icecream'],
    'amount': [45, 60, 60, 45, 100, 140, 190, 170, 55, 70, 20, 45]
}
df = pd.DataFrame(data)

with tab1:
    st.write('Données')
    st.write(df)
    input_sql = st.text_area(label="Entrez votre requête :")
    
    if input_sql != '':
        resutlat_sql = duckdb.sql(input_sql).df()
        st.write(resutlat_sql)