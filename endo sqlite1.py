import pandas as pd
import sqlite3

# 1. Estabelece a conexão com o arquivo do banco de dados
conexao = sqlite3.connect('SQLite.3.csv')

# 2. Define a consulta SQL (ajuste 'tabela_musicas' para o nome real da tabela)
query = "SELECT matricula, nome, turma"

# 3. Lê os dados diretamente para um DataFrame
df_filtrado = pd.read_sql_query(query, conexao)

# 4. Fecha a conexão após o uso
conexao.close()

# Formatação idêntica ao que fizemos anteriormente
formatadores = {col: lambda x: f"{str(x):<20}" for col in df_filtrado.columns}
print(df_filtrado.to_string(index=False, justify='left', formatters=formatadores))
