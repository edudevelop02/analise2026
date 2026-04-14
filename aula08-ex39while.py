'''
versao: 1.1
usando comando while
Desenvolva um codigo que
leia um valor e mostre a tabuada desse valor
e exibir o resultado na tela.
'''
print(f"\nVersao prog.: 1.1") 
print("="*80)
i = 0
result = 0
while i < 10: 
    num = input(f"\n  Digite um numero inteiro ==> ")
    if  num == "" :
        print("\n ERRO: Valor digitado invalido  ")
        exit()
    num =  int(num)
    i2 = 0
    while i2 <= 10:
        result = num * i2
        print(f"Tabuada=> {num} x {i2:2d} = {result}  ")
        i2 = i2 + 1
        

print("="*80)

x = (input("\n Tecle Enter para finalizar ==> ")) 
print(f"\nFinal do programa ")
