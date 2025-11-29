import pandas as pd
import plotly.express as px
import streamlit as st

# título e configuração da página
st.set_page_config(page_title='DASHVACINA', layout='wide')
st.title('VACINAÇÃO - Um Painel de Informações sobre a Vacinação contra COVID-19 - Ano 2021')

# leitura do arquivo CSV
df = pd.read_csv('vacinacao_corrigido.csv')
df.info()  # mostra informações do dataframe

# converter coluna de data
df['date'] = pd.to_datetime(df['date'])

# gráfico de linhas: total de vacinados por país
fig1 = px.line(
    df,
    x='date',
    y='total_vaccinations',
    color='location',
    title='Total de pessoas vacinadas por data e paísSegundo a OMS'
)
fig1.update_layout(xaxis_title='Data', yaxis_title='Total de pessoas vacinadas')
st.plotly_chart(fig1, use_container_width=True)

# filtrar países específicos
df_filtro = df.query(
    'location == "BRAZIL" or location == "INDIA" or location == "UNITED STATES"'
)

# gráfico de pizza: comparação de totalmente vacinados
fig2 = px.pie(
    df_filtro,
    values='people_fully_vaccinated',
    names='location',
    title='Dados comparativos de pessoas totalmente vacinadas'
)
st.plotly_chart(fig2, use_container_width=True)
