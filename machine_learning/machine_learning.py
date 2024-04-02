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
#print(dados_prophet_treino)

#Training and creating the model
modelo = Prophet( weekly_seasonality=True,
                 yearly_seasonality=True,
                  daily_seasonality=False)

modelo.add_country_holidays(country_name='US')
print("\nTreinando e criando o modelo.")
modelo.fit(dados_prophet_treino)

# Creating future forecast dates until the end of 2023
futuro = modelo.make_future_dataframe(periods=150)
print("\nCriando futuras datas para previsão até o final de 2023.")
previsao = modelo.predict(futuro)

# Plotting training, testing, and prediction data

print("\nPlotando os dados de treino, teste e previsões.")
plt.figure(figsize=(14,8))
plt.plot(dados_treino['Date'], dados_treino['Close'], label='Dados de Treino', color='blue')
plt.plot(dados_teste['Date'], dados_teste['Close'], label='Dados Reais (Teste)', color='green')
plt.plot(previsao['ds'], previsao['yhat'], label='Previsão', color='orange', linestyle='--')

plt.axvline(dados_treino['Date'].max(), color='red', linestyle='--', label='Início da Previsão')
plt.xlabel('Data')
plt.ylabel('Preço de Fechamento')
plt.title('Previsão de Preço de Fechamento vs Dados Reais')
plt.legend()
plt.show()