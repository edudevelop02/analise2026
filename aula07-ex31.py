'''
calcula o resto da divisao
desenvolva um codigo que o usuario digite cinco valores 
e apos digitar informe se o valor e par ou impar
'''
print(f"\nCalcula o resto da divisao  -Versao prog.: 1.1")
print("="*80)

for i in range(1,6):
    num = input(f"\n {i}) Digite um numero ==> ")
    if  num == "" :
        print("\n ERRO: Valor invalido  ")
        exit()
#---------------------------------------------
    num =  int(num)
    resto = num % 2
    if resto == 0:
        tipo = "PAR"
    else:
        tipo = "IMPAR"
    print(f"\tResto = {resto} , Numero digitado: {num} e' {tipo}")
#-------------------------------------------

print("="*80)
x = (input("\n Tecle Enter para finalizar ==> ")) 
print(f"\nFinal do programa ")