import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
from prophet import Prophet

# Downloading data from the last four years for a specific asset
dados = yf.download("JNJ", start="2020-01-01", end="2023-12-31", progress=False)
dados = dados.reset_index()
print("\nBaixando dados dos últimos quatro anos para uma ação específica.")
#print(dados)

# Let's divide the data into training (until the end of the semester of 2023) and testing (second semester of 2023)
dados_treino = dados[dados['Date'] < '2023-07-31']
dados_teste = dados[dados['Date'] >= '2023-07-31']
#print("\nDividindo os dados em treino (até o final do semestre de 2023) e teste (segundo semestre de 2023).")

# Preparing data for FBProphet
dados_prophet_treino = dados_treino[['Date', 'Close']].rename(columns={'Date': 'ds', 'Close': 'y'})
print("\nPreparando os dados para o FBProphet.")
print(dados_prophet_treino)