import streamlit as st
import plotly_express as px
import pandas as pd

df = pd.read_csv('vehicles.csv')
st.header('Analisando o Mercado de Veículos')

hist_button = st.button('Criar histograma')

if hist_button:
    st.write(
        'Criando um histograma para o conjunto de dados de anúncios de vendas de carros')

    fig_hist = px.histogram(df, x="odometer")

    st.plotly_chart(fig_hist, use_container_width=True)

scatter_button = st.button('Criar gráfico de dispersão')

if scatter_button:
    st.write(
        'Criando um gráfico de dispersão para o conjunto de dados de anúncios de vendas de carros')

    fig_scatter = px.scatter(df, y="price", x="odometer")

    st.plotly_chart(fig_scatter, use_container_width=True)


'''Aplicativo Web de Análise de Dados de Carros

Este é um aplicativo web criado com Streamlit para visualizar e analisar anúncios de vendas de carros. Aqui, você pode gerar gráficos interativos e explorar os dados de forma fácil e intuitiva.

Funcionalidades

1. Histograma:
   - Cria um histograma da coluna `odometer` (quilometragem) para visualizar a distribuição dos valores.

2. Gráfico de Dispersão:
   - Cria um gráfico de dispersão entre as colunas `odometer` (quilometragem) e `price` (preço) para analisar a relação entre essas variáveis.'''
