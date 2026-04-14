'''
desenvolva um codigo que usando while que
digte uma senha correta e 3 tentativas 
'''
print(f"\nDigite a senha correta  -Versao prog.: 1.2")
print("="*80)
senha_correta = "python123"
senha = ""
tentativas = 0
max_tentativas = 3

#---------------------------------------------
while tentativas < max_tentativas:
    senha = input(f"\n Digite a senha (Tentativa {tentativas + 1}/{max_tentativas}) ==> ")
    if  senha == senha_correta:
        print(f"\nAcesso concedido, Bem Vindo. ")
        break
    else:
        print(f"\nsenha incorreta. ")
        tentativas +=1     # equivale a: tentativas = tentativas + 1 
else:
    print(f"\nVoce ecedeu o numero Maximo de tentativas. Acesso bloqueado ")
#-------------------------------------------

print("="*80)
