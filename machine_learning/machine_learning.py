import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
from prophet import Prophet

# Downloading data from the last four years for a specific asset
dados = yf.download("JNJ", start="2020-01-01", end="2023-12-31", progress=False)
dados = dados.reset_index()
print("\nBaixando dados dos últimos quatro anos para uma ação específica.")
print(dados)