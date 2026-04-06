'''
 

'''

salario =  float(input("\nSalario do funcionario => ")) 

if  salario <= 5000 :
    irrf = 0

elif  salario <= 8000 :
    irrf = salario  * 0.075

else:
    irrf = salario  * 0.27

salario_fim = salario - irrf
print(f"=> Salario Bruto: {salario:.2f} , Imposto IRRF: {irrf:.2f} , Salario Final: {salario_fim:.2f}  ")

print(f"\nFim programa")
