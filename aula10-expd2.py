'''
manipulacao de arquivos de dados

'''
print(f"\nmanipulacao de arquivos de dadosa  -Versao prog.: 1.1")
print("="*80)

import pandas as pd
dados = {
    'cargos' : ["assistente", "analista", "gerente", "diretor"],
    'salarios' : [1000, 2000, 3000, 4000]
}
dados_bi = pd.DataFrame(dados)
print(dados_bi)

x=input("\n*** 1 Tecle Enter para proseguir ===> ")
print(dados_bi[2:4]) 

x=input("\n*** 2 Tecle Enter para proseguir ===> ")
print(dados_bi.shape) 


x=input("\n*** 3 Tecle Enter para proseguir ===> ")
print(dados_bi.to_csv('meus_dados.csv', index=False, sep=';', encoding='utf-8')) 
x=input("\n*** Arquivo CSV exportado com sucesso ! ")
#-------------------------------------------

print("="*80)


