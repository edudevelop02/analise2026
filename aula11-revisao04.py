'''
manipulacao de arquivos de dados

'''
print(f"\nTesta se apto ao servico militar  -Versao prog.: 1.1")
print("="*80)
from datetime import datetime
anoatual = datetime.now().year    # pega o ano atual do sistema
print(f"ANO ATUAL => {anoatual}  ")
data_nasc =  (input("ANO de Nascimento   => "))
data_nasc =  int(data_nasc)    # converte p inteiro
genero=input("Genero 'M' ou 'F' => ").upper()   # uppercase da variavel genero
#genero =        (input("Genero 'M' ou 'F' => "))    # string
idade = anoatual - data_nasc
if  idade >= 18 and genero == "M" :
    print(f"  => {idade} Anos Esta apto para a se alistar  ")
else:
    print(f"  => Idade: {idade} Anos e Genero: {genero} NAO Esta apto para a se alistar  ")
#
print(f"\nFim")

#-------------------------------------------

print("="*80)


