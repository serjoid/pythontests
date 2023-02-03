import pandas as pd
import time
import sys

# Lendo o arquivo CSV
df_csv = pd.read_csv('K3241.K03200Y2.D30114.EMPRECSV')

# Lendo a planilha do Excel
df_excel = pd.read_excel('cnpj_att2.xlsx')

# Calculando o número de iterações
total = df_excel.shape[0]

# Variáveis para controlar a barra de progresso
start_time = time.time()
current = 0

# Iterando sobre as linhas do arquivo excel
for index, row in df_excel.iterrows():
    cnpj = row["cnpj"]
    # Verificando se o valor da coluna "cnpj" existe na coluna "Column1" do arquivo csv
    if cnpj in df_csv["Column1"].values:
        # Encontrando a linha no arquivo csv com o mesmo valor
        match = df_csv.loc[df_csv["Column1"] == cnpj]
        # Copiando os valores dessa linha para as outras colunas no arquivo excel
        df_excel.at[index, "razao_social"] = match.iloc[0]["Column2"]
        df_excel.at[index, "natureza_juridica"] = match.iloc[0]["Column3"]
        df_excel.at[index,
                    "qualificacao_responsavel"] = match.iloc[0]["Column4"]
        df_excel.at[index, "capital_social"] = match.iloc[0]["Column5"]
        df_excel.at[index, "porte_empresa"] = match.iloc[0]["Column6"]
        # ...
    current += 1
    # Atualizando a barra de progresso
    sys.stdout.write("\r[{}{}] {:.0f}% - Tempo restante: {:.2f} segundos".format(
        "=" * int((current / total) * 50),
        " " * (50 - int((current / total) * 50)),
        (current / total) * 100,
        (time.time() - start_time) * (total / current - 1)
    ))
    sys.stdout.flush()

# Salvando as alterações no arquivo excel
df_excel.to_excel("cnpj_att.xlsx", index=False)

# Finalizando a barra de progresso
print("\nFinalizado!")
