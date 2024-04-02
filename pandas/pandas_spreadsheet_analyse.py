import pandas as pd
import plotly.express as px

caminho_arquivo = r"C:\Users\Vitor Cardoso\Desktop\GitHub_Training\Alura_Imersao_Python\spreadsheet\acoes pura.xlsx"

# Importing spreadsheet data into the Data Frame (DF) variable

df_principal = pd.read_excel(caminho_arquivo, sheet_name="Principal")
print("\nImportando dados da aba \"Principal\" da planilha \"acoes pura\"")
#print(df_principal.head(10))

df_total_acoes = pd.read_excel(caminho_arquivo, sheet_name="Total_de_acoes")
print("\nImportando dados da aba \"Total_de_acoes\" da planilha \"acoes pura\"")
#print(df_total_acoes.head(10))

df_ticker = pd.read_excel(caminho_arquivo, sheet_name="Ticker")
print("\nImportando dados da aba \"Ticker\" da planilha \"acoes pura\"")
#print(df_ticker.head(10))

df_chatgpt = pd.read_excel(caminho_arquivo, sheet_name="ChatGPT")
print("\nImportando dados da aba \"ChatGPT\" da planilha \"acoes pura\"")
#print(df_chatgpt.head(10))