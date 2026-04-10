'''
calcula o resto da divisao
desenvolva um codigo que imprima na tela os numeros de 15 a 30 
e diga cada um deles se e par ou impar
'''
print(f"\nCalcula o resto da divisao  -Versao prog.: 1.1")
print("="*80)

#---------------------------------------------
for i in range(15,31):
#    num = input(f"\n {i}) Digite um numero ==> ")
    num =  int(i)
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