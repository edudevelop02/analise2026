'''
versao: 2.01
Desenvolva um codigo que
leia um valor e mostre a tabuada desse valor
e exibir o resultado na tela.
'''
print(f"\nVersao prog.: 1.1")
print("="*80)
#i = 0
result = 0
for i in range(10):
    num = input(f"\n  Digite um numero ==> ")
    if  num == "" :
        print("\n ERRO: Valor invalido  ")
        exit()
    num =  int(num)
    for i2 in range(0,11):
        result = num * i2
        print(f"Tabuada=> {num} x {i2} = {result}  ")

#print(f"=> Somatorio = {soma}  ")
print("="*80)

x = (input("\n Tecle Enter para finalizar ==> ")) 
print(f"\nFinal do programa ")
