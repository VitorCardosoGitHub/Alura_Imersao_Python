import pandas as pd
import plotly.express as px

caminho_arquivo = r"C:\Users\Vitor Cardoso\Desktop\GitHub_Training\Alura_Imersao_Python\spreadsheet\acoes pura.xlsx"

# Importing spreadsheet data into the Data Frame (DF) variable

df_principal = pd.read_excel(caminho_arquivo, sheet_name="Principal")
print("\nImportando dados da aba \"Principal\" da planilha \"acoes pura\".")
#print(df_principal.head(10))

df_total_acoes = pd.read_excel(caminho_arquivo, sheet_name="Total_de_acoes")
print("\nImportando dados da aba \"Total_de_acoes\" da planilha \"acoes pura\".")
#print(df_total_acoes.head(10))

df_ticker = pd.read_excel(caminho_arquivo, sheet_name="Ticker")
print("\nImportando dados da aba \"Ticker\" da planilha \"acoes pura\".")
#print(df_ticker.head(10))

df_chatgpt = pd.read_excel(caminho_arquivo, sheet_name="ChatGPT")
print("\nImportando dados da aba \"ChatGPT\" da planilha \"acoes pura\".")
#print(df_chatgpt.head(10))

# filtering columns from "Principal" dataframe
df_principal = df_principal[["Ativo", "Data", "Último (R$)", "Var. Dia (%)"]].copy()
print("\nFiltrando colunas do dataframe \"Principal\".")
#print(df_principal)

# Renaming columns to make names more Python-friendly
df_principal = df_principal.rename(columns={'Último (R$)':'valor_final','Var. Dia (%)':'var_dia_pct'}).copy()
print("\nRenomeando colunas para deixar nomes mais amigáveis ao python.")
#print(df_principal)

# Creating new columns for analysis - "Var_pct" and "Var_inicial"
df_principal['Var_pct'] = df_principal['var_dia_pct']/100
df_principal['Var_inicial'] = df_principal['valor_final']/(df_principal['Var_pct']+1)
print("\nCriando novas colunas para analise - \"Var_pct\" e \"Var_inicial\".")
#print(df_principal)

# Merge between df_principal and df_total_acoes - Codigo
df_principal = df_principal.merge(df_total_acoes, left_on='Ativo', right_on='Código',how='left')
print("\nMerge entre df_principal e df_total_acoes - Codigo.")
#print(df_principal)

# Removing duplicate column - codigo
df_principal = df_principal.drop(columns=['Código'])
print("\nRemovendo coluna duplicada - codigo.")
#print(df_principal)

# Creating new analysis column - VARIACAO_RS
df_principal['variacao_rs'] = (df_principal['valor_final'] - df_principal['Var_inicial'])*df_principal['Qtde. Teórica']
print("\nCriando nova coluna de analise - VARIACAO_RS.")
#print(df_principal)

# Adjusting formatting for float type
pd.options.display.float_format = '{:.2f}'.format
print("\nAjustando formatação para tipo float.")
#print(df_principal)

# Adjusting formatting of the "Qtde. Teorica" column for int
df_principal['Qtde. Teórica'] = df_principal['Qtde. Teórica'].astype(int)
print("\nAjustando formatacao da coluna \"Qtde. Teorica\" para int.")
#print(df_principal)

# Adjusting the name of the "Qtde. Teorica" column 
df_principal = df_principal.rename(columns={'Qtde. Teórica':'Qtd_teorica'}).copy()
print("\nAjustando o nome da coluna \"Qtde. Teorica\".")
#print(df_principal)

# Logical validation with if + new column - check if the variation has gone up "Subiu" or down "Desceu"
df_principal['Resultado'] = df_principal['variacao_rs'].apply(lambda x: 'Subiu' if x > 0 else ('Desceu' if x < 0 else 'Estavel'))
print("\nValidação lógica com if + nova coluna - verificando se a variação subiu ou desceu.")
#print(df_principal)

# Merge with "ativo" vs "nome da empresa"
df_principal = df_principal.merge(df_ticker, left_on='Ativo', right_on='Ticker',how='left')
print("\nMerge with \"ativo\" vs \"nome da empresa\".")
print(df_principal)

# Removing column 'Ticker'
df_principal = df_principal.drop(columns=['Ticker'])
print("\nRemovendo coluna \"Ticker\".")
print(df_principal)

# Merge with 'nome' vs 'segmento'
df_principal = df_principal.merge(df_chatgpt, left_on='Nome', right_on='Nome da Empresa',how='left')
print("\nMerge entre \"nome\" vs \"segmento\".")
#print(df_principal)

# Removing column 'Nome da Empresa'
df_principal = df_principal.drop(columns=['Nome da Empresa'])
print("\nRemovendo coluna \"Nome da Empresa\".")
print(df_principal)

# Renaming column 'Idade (em anos)'
df_principal = df_principal.rename(columns={'Idade (em anos)':'Idade'})
print("\nRenomeando coluna \"Idade (Em anos)\".")
#print(df_principal)

# Logical validation with if + new column - checking age of the company
df_principal['Cat_idade'] = df_principal['Idade'].apply(
    lambda x: 'Mais de 100' 
    if x > 100 else ('Menos de 50' 
    if x < 50 else 'Entre 50 e 100'))
print("\nValidação lógica com if + nova coluna - Conferindo idade da empresa.")
print(df_principal)