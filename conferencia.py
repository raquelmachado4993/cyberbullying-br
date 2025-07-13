# encoding: iso-8859-1
import pandas as pd

# Faz o upload do arquivo do dataset, é um csv
# uploaded = open('./dataset.csv')
# df = pd.read_csv('./dataset.csv')
df =  fun.carregarCSV('./dataset.csv')
# Lê o csv
print("Primeiras linhas:")
print(df.head())

# Mostra total de linhas
print(f"\nTotal de linhas: {len(df)}")

# Clean up column names by stripping whitespace
df.columns = df.columns.str.strip()

# Faz uma limpeza simples: remove espaços e converte para minúsculas
df['Classific'] = df['Classific'].astype(str).str.strip().str.lower()

# Aqui mostra quantos comentários foram classificados como cyberbullying e quantos foram classificados como n_cyberbullying
cyberbullying_count = (df['Classific'] == 'cyberbullying').sum()
nao_cyberbullying_count = (df['Classific'] == 'n_cyberbullying').sum()

# Mostra o resultado
print(f'Total de comentários cyberbullying: {cyberbullying_count}')
print(f'Total de comentários n_cyberbullying: {nao_cyberbullying_count}')
print(f'Total geral considerado: {cyberbullying_count + nao_cyberbullying_count}')