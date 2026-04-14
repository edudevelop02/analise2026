'''
desenvolva um codigo que:
Usando comando while verifique qual dos numeros digitados e o maior
'''
print(f"\nverifique qual dos numeros digitados e o maior  -Versao prog.: 1.1)")
print("="*80)
#---------------------------------------------
i=1
maior = 0
while i <= 3:
    v=int(input(f"\n {i} Digite um numero==> "))
    if  v > maior:
        maior = v
    i=i+1
print(f"Maior = {maior}")    
#-------------------------------------------

print("="*80) 