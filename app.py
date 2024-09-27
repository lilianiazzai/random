
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import psycopg2

###################
# CONNECTION

conn_params = {
    'dbname': 'nome_do_banco',    # Nome do seu banco de dados
    'user': 'seu_usuario',         # Seu usuário do PostgreSQL
    'password': 'sua_senha',       # Sua senha do PostgreSQL
    'host': 'localhost',           # Endereço do servidor (pode ser localhost)
    'port': '5432'                 # Porta padrão do PostgreSQL
}

def consulta(query):
    try:
        conn = psycopg2.connect(**conn_params)
        print('conexão com o basnco de dados estabelecida com sucesso')

        df = pd.read_sql_query(query, conn)

        return df
    except Exception as e:
        print(f"Ocorreu um erro ao conectar ao banco de dados: {e}")

dataframe_novo = consulta("SELECT * FROM Libre;")


#####################################################
#STREAMLIT

# css = '''
# <style>
#     section.main > div {max-width:75rem}
# </style>
# '''
# st.markdown(css, unsafe_allow_html=True)

# Configurar a página para largura total (comentar o código acima)
st.set_page_config(layout="wide")

# Criar o menu lateral
st.sidebar.image("ic_launcher_round.png", use_column_width=False)  # Ícone
st.sidebar.text_input("🔍 Pesquisar", placeholder="Pesquisar pacientes...")  # Campo de pesquisa
st.sidebar.button("UBSs")

# Carregar os dados CSV
df = pd.read_csv('results.csv')

# Configurar o título principal
st.title("Dados Gerais")

# Layout em grid com 3 gráficos de barras (Refeições)
st.subheader("Refeições")
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Café da Manhã")
    plt.bar(df['Data'], df['Cafe_da_Manha'], color='teal')
    plt.xticks(rotation=45)
    st.pyplot(plt)
    plt.clf()  # Limpar a figura

with col2:
    st.subheader("Almoço")
    plt.bar(df['Data'], df['Almoco'], color='cyan')
    plt.xticks(rotation=45)
    st.pyplot(plt)
    plt.clf()  # Limpar a figura

with col3:
    st.subheader("Jantar")
    plt.bar(df['Data'], df['Jantar'], color='royalblue')
    plt.xticks(rotation=45)
    st.pyplot(plt)
    plt.clf()  # Limpar a figura

# Layout com gráficos para sono e livre (2ª linha)
st.subheader("Sono e Libre")

col4, col5, col6, col7 = st.columns(4)

# Gráfico de pizza com furo no meio (sono)
with col4:
    st.subheader("Sono")
    fig1, ax1 = plt.subplots()
    ax1.pie(df['Sono'].value_counts(), labels=df['Sono'].unique(), autopct='%1.1f%%', startangle=90)
    centre_circle = plt.Circle((0, 0), 0.70, fc='white')
    fig1.gca().add_artist(centre_circle)
    ax1.axis('equal')
    st.pyplot(fig1)
    plt.clf()  # Limpar a figura

# Gráfico de barras horizontal (livre)
with col5:
    st.subheader("Medições")
    fig1, ax1 = plt.subplots()
    ax1.pie(df['Sono'].value_counts(), labels=df['Sono'].unique(), autopct='%1.1f%%', startangle=90)
    centre_circle = plt.Circle((0, 0), 0.70, fc='white')
    fig1.gca().add_artist(centre_circle)
    ax1.axis('equal')
    st.pyplot(fig1)
    plt.clf()  # Limpar a figura
    

with col6:
    st.subheader("Libre")
    plt.barh(df['Data'], df['Cafe_da_Manha'], color='teal')
    plt.xlabel('Quantidade de medições')
    st.pyplot(plt)
    plt.clf()  # Limpar a figura
    
# Gráfico de barras vertical (diário alimentar)    
with col7:
    st.subheader("Diário Alimentar")
    plt.bar(df['Data'], df['Diario_Alimentar'], color='turquoise')
    plt.xticks(rotation=45)
    st.pyplot(plt)
