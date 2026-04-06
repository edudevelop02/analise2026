# armazene peso e altura da pessoa e calcule o indice de massa corporal IMC
#imc = peso / (altura x altura)

peso   =  float(input("\nDigite o peso  =>"))      # inteiro
altura =  float(input(  "Digite o altura=>"))   # real Float

imc = peso / (altura * altura)
#imc = peso / ( altura**)

print(f"\nSeu IMC  = {imc} ")
