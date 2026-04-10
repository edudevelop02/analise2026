'''
calcula o resto da divisao
desenvolva um codigo que leia 10 medias de aluno e no momento 
que esta lendo mostre se o aluno esta aprovado se for maior que 5 
ou em recuperacao no caso contrario;
'''
print(f"\nCalcula se aprovado ou nao  -Versao prog.: 1.2")
print("="*80)
media = 0
#---------------------------------------------
for i in range(1,11):
    media = input(f"\n Digite a MEDIA {i} ==> ")
    if  media == "" :
        print("\n ERRO: Valor invalido  ")
        exit()
    media = float(media)
    if media > 5:
        tipo = "APROVADO"
    else:
        tipo = "EM RECUPERAÇÃO"
    print(f"\tCom Media = {media} , Aluno esta {tipo}")
#-------------------------------------------

print("="*80)
x = (input("\n Tecle Enter para finalizar ==> ")) 
print(f"\nFinal do programa ")