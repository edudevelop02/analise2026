'''
desenvolva um codigo que leia o salario de um funcionario,
se o salario for maior que 5000 calcula irrf de 7,5% sobre o salario
se for menor que 5000 NAO PAGA imposto e
se salario maior que 8000 imposto e de 27%. 
Ao final mostre o salario bruto, o valor do imposto pago e salario final com o desconto

'''
print(f"\nCalcular valor do IRRF do salario informado  -Versao prog.: 1.1")
print("="*80)
salario =  float(input("\nSalario do funcionario => ")) 

if  salario <= 5000 :
    irrf = 0

elif  salario <= 8000 :
    irrf = salario  * 0.075

else:
    irrf = salario  * 0.27

salario_fim = salario - irrf
print(f"=> Salario Bruto: {salario:.2f} , Imposto IRRF: {irrf:.2f} , Salario Final: {salario_fim:.2f}  ")
#
print(f"\nFinal do programa")

#-------------------------------------------

print("="*80)


