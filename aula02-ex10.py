'''
7) Desenvolva um código python que leia o nome de uma pessoa
e o ano de nascimento, ao final mostre a seguinte mensagem
"olá fulano você tem x anos"
pegar nome e ano de nascimento da pessoa e calcular e exibir sua idade
# 
# '''

nome     =      input("\nNome da Pessoa    =>")     # string
ano_nasc =  int(input("\nAno de Nascimento =>"))    # captura ano e converte p/ inteiro

idade  = (2026 - ano_nasc)
#
print(f"\nOla {nome}, voce tem {idade} anos \n")

