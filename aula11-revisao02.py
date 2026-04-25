'''
manipulacao de arquivos de dados

'''
print(f"\ncalcule o IMC da pessoa.  -Versao prog.: 1.1")
print("="*80)
peso   =  float(input("\nDigite o peso  =>"))      # inteiro
altura =  float(input(  "Digite o altura=>"))   # real Float

imc = peso / (altura * altura)
#imc = peso / ( altura**)

print(f"\nSeu IMC  = {imc:.4f} ")   # :.4f  exibe valor tipo float com 4 casas decimais a direita

#-------------------------------------------

print("="*80)


