'''
calcula o resto da divisao
'''
print(f"\nCalcula o resto da divisao  -Versao prog.: 1.1")
print("="*80)

for i in range(10):
    num = input(f"\n  Digite um numero ==> ")
    if  num == "" :
        print("\n ERRO: Valor invalido  ")
        exit()

    num =  int(num)
    resto = num % 2
    print(f"Resto ==> {resto} ")

print("="*80)

x = (input("\n Tecle Enter para finalizar ==> ")) 
print(f"\nFinal do programa ")