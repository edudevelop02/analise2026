'''
criar uma funcao que receba dois numeros e retorne o maior deles

'''
print(f"\nFuncao que receba dois numeros e retorne o maior deles  -Versao prog.: 1.1")
print("*"*80)

# 1. Definimos inicialmente a funcao que sabe somar
#---------------------------------------------
def maior_num(x,y):        # funcao predefinida para somar
    if  x > y:
        return  x
    elif x == y:
        return  "são iguais"
    else:
        return  y
#
# digitar um numero na tela
for i in range(5):
    try:
        a=int(input("Digite um valor A = "))
        b=int(input("Digite um valor B = "))
    except ValueError:
        print(f"   *** Entrada invalida. Digite um numero ! ***")
        break
        #exit()

    # Mostramos o resultado na tela
    print(f"  => O maior numero é {maior_num(a,b)} ")

#-------------------------------------------

print("="*80)


