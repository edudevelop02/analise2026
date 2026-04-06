'''
ler um valor de um produto e de um desconto de acordo com a tabela de valores abaixo
valor      - desconto
> 500      - 20%
100 a 499  - 15%
<100       -  5% 
mostrar valor do desconto e valor final do produto  

'''
print(f"\nDigite o valor do produto : \n")
valor =  float(input("Valor =>"))    # inteiro
if  valor  < 100:
    valor_desc = valor * 0.05
    valor_final = valor - valor_desc
    perc=5

elif valor >= 100 and valor <= 499 :
    valor_desc = valor * 0.15
    valor_final = valor - valor_desc
    perc=15

else:
    valor_desc = valor * 0.20
    valor_final = valor - valor_desc
    perc=20
print(f"  =>Valor R${valor} - {perc}% desconto (R${valor_desc}) =>R${valor_final}  ")

print(f"\nFim programa")
