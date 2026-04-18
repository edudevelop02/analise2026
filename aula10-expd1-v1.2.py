'''
manipulacao de arquivos de dados

'''
print(f"\nmanipulacao de arquivos de dadosa  -Versao prog.: 1.2")
print("="*80)

import pandas as pd

df = pd.read_csv('ClassicDisco.csv')

# 1. Filtramos as colunas desejadas
# 2. Usamos o .head(15) para pegar as 15 primeiras linhas
colunas = ['Track', 'Artist', 'Album', 'Year', 'Duration']
df_filtrado = df[colunas].head(10)   # head(10) exibe as 10 primeiras linhas
print(df_filtrado.to_string())
x=input("\n*** 1 Tecle Enter para proseguir ===> ")

df_filtrado = df[colunas].tail(10)   # tail(10) exibe as 10 ULTIMAS linhas
print(df_filtrado.to_string())
x=input("\n*** 2 Tecle Enter para proseguir ===> ")


print(df_filtrado.to_string())
x=input("\n*** 3 Tecle Enter para proseguir ===> ")

print(df_filtrado.shape)    # verifica o numero de linhas


# Criamos um formatador que força a string a ter espaços à direita (alinhando à esquerda)
# O número 30 define a largura da coluna, ajuste conforme o tamanho dos nomes das músicas
formatters = {
    'Track': lambda x: f"{x:<30}"
}
print(df_filtrado.to_string(index=False, justify='left', formatters=formatters))

x=input("\n*** 4 Tecle Enter para proseguir ===> ")

# Criamos um formatador para cada coluna selecionada

# O {:<20} garante 20 espaços de largura com alinhamento à esquerda
formatadores = {col: lambda x: f"{str(x):<20}" for col in df_filtrado.columns}

# Imprimimos usando os formatadores e justificando o cabeçalho
print(df_filtrado.to_string(index=False, justify='left', formatters=formatadores))

x=input("\n*** Tecle Enter para proseguir ===> ")
#-------------------------------------------

print("="*80)


