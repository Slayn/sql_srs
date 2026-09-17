import duckdb
import streamlit as st

# Connection et récupération de la données dans la base duckdb
con = duckdb.connect(database="data/exercices_sql_tables.duckdb", read_only=False)
# data = con.execute("SELECT * FROM data").df()

# Défnition de la solution
# solution_sql = """
# SELECT * FROM data
# WHERE product_name = 'redbull'
# """
# solution_df = duckdb.sql(solution_sql).df()


# Titre du programme
st.write("SQL - SRS")


# Menu gauche
with st.sidebar:
    theme = st.selectbox(
        "Choix du sujet à réviser :",
        ("cross_joins", "GroupBy", "Windows Function"),
        index=None,
        placeholder="Selection du sujet",
    )
    st.write("Sujet choisi : ", theme)

    exercice = con.execute(f"SELECT * FROM memory_state WHERE theme = '{theme}'").df()
    st.write(exercice)

# Header / toujours affiché
input_sql = st.text_area(label="Entrez votre requête :", key="user_input")

# if input_sql != "":
#     result = duckdb.sql(input_sql).df()

#     # On force l'ordre des colonnes du résultat en fonction de la solution pour mieux gérer le compare
#     try:
#         result = result[solution_df.columns]
#     except KeyError:
#         st.write("Nombre de colonne incorrect")

#     # Validation du résultat
#     try:
#         compare = result.compare(solution_df)
#         st.write("Parfait ! C'est le bon résultat")
#         st.dataframe(result)
#     except ValueError:
#         st.write(r"/!\ Le résultat n'est pas celui attendu")
#         st.dataframe(result)


# # Tab list
# tab1, tab2 = st.tabs(["Tables", "Solution"])

# # Tabs content
# with tab1:
#     st.write("Table : data")
#     st.dataframe(data)
#     st.write("Résultat attendu :")
#     st.dataframe(solution_df)

# with tab2:
#     st.write(solution_sql)
