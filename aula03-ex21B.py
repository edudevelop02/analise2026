'''
print(f"\nVersao prog.: 1.1")
#Desenvolva um código python que leia o salário
#de um funcionário se o salário for maior que 5000
#1 - <=5000 ir=0
#2 - >5000 ate 8000 ir 7,5%
#3 - >8000 ir 27
#calcule  o irrf que será 7,5% sobre o salário
#se for menor que 5000 não paga imposto iR 
#e se for maior que 8000 o imposto será 
#27%. Ao final mostre: o salário, 
#o valor do imposto pago e salario final.

'''
print("="*80)
salario =  input("\nSalario do funcionario ==> ")
if  salario == "" :
    print("\n ERRO: Valor do salario vazio  ")
    exit()
#if  salario.isnumeric() is False :
#    print("\n ERRO: Digitado valor NAO NUMERICO  ")
#    exit()

salario =  float(salario)
#salario =  float(input("\nSalario do funcionario => ")) 

if  salario <= 5000 :
    irrf = 0

elif  salario <= 8000 :
    irrf = salario  * 0.075

else:
    irrf = salario  * 0.27

salario_fim = salario - irrf
print("="*80)
print(f"=> Salario Bruto: {salario:.2f} , Imposto IRRF: {irrf:.2f} , Salario Final: {salario_fim:.2f}  ")
print("="*80)

x = (input("\n Tecle Enter para finalizar ==> ")) 
print(f"\nFinal do programa 3.3")