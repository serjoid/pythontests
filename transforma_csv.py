import pandas as pd

# Lista de nomes de colunas
colunas = ['Column1', 'Column2', 'Column3',
           'Column4', 'Column5', 'Column6', 'Column7']

# Leitura do arquivo csv sem cabeçalho
df = pd.read_csv('K3241.K03200Y2.D30114.EMPRECSV',
                 sep=';', encoding='ISO-8859-1')

# Atribuição dos nomes de colunas ao dataframe
df.columns = colunas

# Gravação do dataframe no arquivo csv com o cabeçalho incluído
df.to_csv("K3241.K03200Y2.D30114.EMPRECSV", index=False)
