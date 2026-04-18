'''
manipulacao de arquivos de dados

'''
print(f"\nmanipulacao de arquivos de dadosa  -Versao prog.: 1.1")
print("*"*80)

import pandas as pd
df = pd.read_csv('ClassicDisco.csv')
print(df.to_string())


#-------------------------------------------

print("="*80)


