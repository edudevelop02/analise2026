'''
criar uma funcao que receba dois numeros e retorne o maior deles

'''
print(f"\nFuncao de calculadora basica  -Versao prog.: 1.1")
print("*"*80)

# 1. Definimos inicialmente a funcao que sabe somar
#---------------------------------------------
def somar(a,b):        # funcao predefinida para somar
    return a + b
#
def subtrair(a,b):     # funcao predefinida subtrair
    return a - b
#
def multi(a,b):        # funcao predefinida para multiplicar
    return a * b
#
def divi(a,b):        # funcao predefinida para multiplicar
    if b!= 0:
        return a / b
    else:
        return "Valor invalido ! "
        ##print("Valor invalido !")
#
#   digitar um numero na tela
escolha = ""
while escolha != "0":
    escolha = input("Digite uma opcao: 1-somar, 2-subtrair, 3-multiplicar, 4-divisao = ")
    try:
        num1=int(input("Digite o primeiro numero : "))
        num2=int(input("Digite o segundo  numero : "))
        if escolha == "1":
            x = somar(num1,num2)
        elif escolha == "2":
            x = subtrair(num1,num2)
        elif escolha == "3":
            x = multi(num1,num2)
        else:
            x = divi(num1,num2)

# Mostramos o resultado na tela
        print(f"  => O resultado é : {x} ")        
    except ValueError:
        print(f"   *** Entrada invalida. Digite um numero ! ***")
        exit()
else:
    print(f"   *** operacao terminada ! ***")

#-------------------------------------------

print("="*80)


