'''
uso de funcoes predefinidas def()
'''
# 1. Definimos inicialmente a funcao que sabe somar
#---------------------------------------------
def somar(a,b):        # funcao predefinida para somar
    resultado = a + b
    return resultado
#
def subt(i,y):        # funcao predefinida subtrair
    x = i - y
    return x
#
print(f"\nFuncao para somar e subtrair  -Versao prog.: 1.1")
print("="*80)
# 2. Criamos as variaveis com os valores
numero1 = 12
numero2 = 5
a = 2    # essa variavel 'a' é outra variavel fora da funcao com o mesmo nome mas valor diferente

# 3. Chamamos a funcao e guardamos o que ela calculou em outra variavel
total1 = somar(numero1, numero2)
total2 = subt(numero1, numero2)
numero1 = 500
total3 = subt(numero2, numero1)

# 4. Mostramos o resultado na tela
print("A soma        é :", total1)
print("A subtracao 1 é :", total2)
print("A subtracao 2 é :", total3)
print("a =", a)

#-------------------------------------------

print("="*80)
