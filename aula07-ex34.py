'''
desenvolva um codigo que:
leia 5 idades e diga se cada um é maior de idade,
menor de idade ou idoso com 65 ou mais.
'''
print(f"\nCalcula idade  -Versao prog.: 1.1)")
print("="*80)
#idade = 0
#---------------------------------------------
for i in range(1,6):
    idade = input(f"\n Digite a IDADE ==> ")
    if  idade == "" :
        print("\n ERRO: Valor invalido  ")
        exit()
    idade = int(idade)
    if idade >= 65:
        tipo = "IDOSO"
    elif idade >= 18:
        tipo = "MAIOR DE IDADE"
    else:
        tipo = "Menor de Idade"

    print(f"\tCom idade = {idade} , pessoa {tipo} ")
#-------------------------------------------

print("="*80)
x = (input("\n Tecle Enter para finalizar ==> ")) 
print(f"\nFinal do programa ")