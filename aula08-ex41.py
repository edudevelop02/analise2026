'''
desenvolva um codigo queusando while que
digte um nome e imprima , e so encerre o programa ao digitar 'SAIR' 
'''
print(f"\nDigitar nomes e fazer upper case  -Versao prog.: 1.2")
print("="*80)
nome = ""
#---------------------------------------------
while nome != "SAIR":
    nome = input(f"\n Digite um Nome ==> ").upper()   # converte string para maiusculo
    if  nome == "SAIR" :
        break
    print(f"\tNome digitado => {nome} ")
#-------------------------------------------
print(f"\nFinal do programa ")

print("="*80)
