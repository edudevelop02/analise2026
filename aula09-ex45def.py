'''
criar uma funcao que calcule 10% de um valor
'''
# 1. Definimos inicialmente a funcao que sabe somar
#---------------------------------------------
def porc(x):        # funcao predefinida para somar
    p = x * 0.1
    return p
#
print(f"\nFuncao para calcular percentual de um numero  -Versao prog.: 1.1")
print("="*80)
# digitar um numero na tela
v=int(input("Digite um valor: "))
y = porc(v)

# Mostramos o resultado na tela
print(f" 10% de {v} = {y}")

#-------------------------------------------

print("="*80)
