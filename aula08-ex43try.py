'''
desenvolva um codigo que usando while e try que
digite notas entre 0 e 10
'''
print(f"\nDigite a nota correta  -Versao prog.: 1.2")
print("="*80)
nota = 0
#---------------------------------------------
while nota >= 0 and nota <= 10:
    try:
        nota = int(input(f"\n Digite a Nota entre 0 e 10 ==> "))
    except ValueError:
        print(f"\n  Entrada inalida. Digite um numero !")

print(f"\nNota Invalida registrada: {nota}")
#-------------------------------------------

print("="*80)
