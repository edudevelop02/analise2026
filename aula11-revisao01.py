'''
manipulacao de arquivos de dados

'''
print(f"\ncalcule data nascim.  -Versao prog.: 1.1")
print("="*80)
#anoatual = 2026
from datetime import datetime
anoatual = datetime.now().year    # pega o ano atual do sistema
idade   =  int(input("\nDigite a Idade  =>"))      # inteiro

anonasc = anoatual - idade

print(f"Ano Nascimento  = {anoatual - idade} ")

#-------------------------------------------

print("="*80)


