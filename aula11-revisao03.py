'''
manipulacao de arquivos de dados

'''
print(f"\nCalcular Medias de 3 notas  -Versao prog.: 1.1")
print("="*80)
nota1   =  float(input("\nDigite primeira Nota  =>"))      # float
nota2   =  float(input("\nDigite segunda  Nota  =>"))      # float
nota3   =  float(input("\nDigite terceira Nota  =>"))      # float

media  = (nota1 + nota2 + nota3) / 3
print(f"\nMedia {media:.2f} ")   # :.2f  exibe valor tipo float com 2 casas decimais a direita

if  media >= 6:
    print(f" APROVADO ")   # :.2f  exibe valor tipo float com 2 casas decimais a direita
else:
    print(f" Recuperacao ")

#-------------------------------------------

print("="*80)


