import duckdb
import streamlit as st


def get_all_exercice_information(theme):
    # Récupération des informations sur l'exercice
    exercice = con.execute(f"SELECT * FROM memory_state WHERE theme = '{theme}'").df()

    # Récupération de la solution
    answer_filename = f"{exercice.loc[0, 'exercise_name']}.sql"
    with open(f"answers/{answer_filename}") as f:
        answer = f.read()

    # Création d'un dictionnaire
    all_exercice_information = {
        "info": exercice,
        "reponse": answer,
    }

    return all_exercice_information


# __main__

# Connection et récupération de la données dans la base duckdb
con = duckdb.connect(database="data/exercices_sql_tables.duckdb", read_only=False)


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

    # exercice = con.execute(f"SELECT * FROM memory_state WHERE theme = '{theme}'").df()
    try:
        all_exercice_information = get_all_exercice_information(theme)
        exercice = all_exercice_information["info"]
        reponse = all_exercice_information["reponse"]
    except:
        exercice = []
        reponse = ""

    st.write(exercice)

# Header / toujours affiché
input_sql = st.text_area(label="Entrez votre requête :", key="user_input")

if input_sql != "":
    try:
        result = con.execute(input_sql).df()
        st.write(result)
    except duckdb.CatalogException as e:
        st.write("Syntaxe SQL invalide")
        st.write(f"{e}")

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


# Tab list
tab1, tab2 = st.tabs(["Tables", "Solution"])

# Tabs content
with tab1:
    try:
        exercice_tables = exercice.loc[0, "tables"]

        for table in exercice_tables:
            st.write(f"Table : {table}")
            table_content = con.execute(f"SELECT * FROM {table}").df()
            st.dataframe(table_content)
    except:
        st.write("")

with tab2:
    st.write(reponse)
