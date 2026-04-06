'''

'''
print(f"\nCalcular Medias de 3 notas \n")
nota1 =  float(input("Nota 1 =>"))    # real Float
nota2 =  float(input("Nota 2 =>"))    # real Float
nota3 =  float(input("Nota 3 =>"))    # real Float

media  = (nota1 + nota2 + nota3 ) / 3
print(f"\nMedia das notas ==> {media} \n")
if  media >= 6 :
    print("APROVADO")
else:
    print("RECUPERACAO")
#
print(f"\nFim")
