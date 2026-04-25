'''
usando for 
desenvolva um codigo que some os valores entre 1 e 10 automaticamente

'''
print(f"\nsome os valores entre 1 e 10 automaticamente  -Versao prog.: 1.1")
print("="*80)

soma = 0
for i in range(0,5):
    n = int(input(f"{i} Digite um numero => "))
    print(f"{n} + {soma} = {n} ")
    soma = soma + n
#
print(f"somatorio => {soma} ")
#
print(f"\nFinal do programa")

#-------------------------------------------

print("="*80)


