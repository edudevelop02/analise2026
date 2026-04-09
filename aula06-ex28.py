'''
Desenvolva um codigo que
seja capas de coletar uma sequencia de 5 numeros inteiros fornecidos pelo usuario, 
Ao final da leitura desses valores, o programa deve calcular o somatorio total 
e exibir o resultado na tela.
'''
print(f"\nVersao prog.: 1.1")
print("="*80)
#i = 0
soma = 0
for i in range(1,6):
    num =  int(input(f" {i}) Digite um numero ==> "))
    soma = soma + num

print(f"=> Somatorio = {soma}  ")
print("="*80)

x = (input("\n Tecle Enter para finalizar ==> ")) 
print(f"\nFinal do programa ")