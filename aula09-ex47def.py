'''
criar uma funcao que receba o lado de um quadrado e retorne o valor da area calculada

'''
print(f"\nFuncao para retorne o valor da area calculada  -Versao prog.: 1.1")
print("*"*80)

# 1. Definimos inicialmente a funcao que sabe somar
#---------------------------------------------
def area_quad(x):        # funcao predefinida para somar
    area = x ** 2        # operador de potenciacao (**)
    return area
#
# digitar um numero na tela
try:
    v=int(input("Digite um valor : "))
except ValueError:
#   print(f"\033[F\033[K *** Entrada invalida. Digite um numero ! ***")
    print(f"   *** Entrada invalida. Digite um numero ! ***")
    exit()

# Mostramos o resultado na tela
print(f"  => Area do quadrado de lado {v} é = {area_quad(v)} ")

#-------------------------------------------

print("="*80)

import time
for i in range(5):
    print(i, end=" ", flush=True)   # flush garante a atualização imediata na tela
    time.sleep(0.2)                 # temporiza 0.2 segundos entre cada print no loop

