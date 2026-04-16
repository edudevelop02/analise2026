'''
criar uma funcao que verifique se o numero e impar ou par
'''
print(f"\nFuncao para verificar se o numero e impar ou par  -Versao prog.: 1.1")
print("*"*80)

# 1. Definimos inicialmente a funcao que sabe somar
#---------------------------------------------
def tipo_num(x):        # funcao predefinida para somar
    if (x % 2) == 1:
        return "IMPAR"
    else:
        return "PAR "
    return tipo
#
# digitar um numero na tela
try:
    v=int(input("Digite um Numero: "))
except ValueError:
#   print(f"\033[F\033[K *** Entrada invalida. Digite um numero ! ***")
#           \33[F   retorna cursor para linha anterior
#           \33[K   apaga a linha 
    print(f"   *** Entrada invalida. Digite um numero ! ***")
    exit()

# Mostramos o resultado na tela
print(f"  => O Numero {v} é {tipo_num(v)} ")

#-------------------------------------------

print("="*80)

import time
for i in range(5):
    print(i, end=" ", flush=True)   # flush garante a atualização imediata na tela
    time.sleep(0.2)                 # temporiza 0.2 segundos entre cada print no loop

