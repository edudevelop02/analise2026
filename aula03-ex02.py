'''

'''
print(f"\nDIGITE SEU GENERO : \n")
genero =  input("Digite Genero M ou F  => ")    # string
genero=genero.upper()   # uppercase da variavel genero
print(genero)
if  genero == "M" or genero == "m":
    print("MASCULINO")
else:
    if  genero == "F" or genero == "m":
        print("FEMININO")
    else:
        print("ERRO: DIGITE M ou F ")
#
print(f"\nFim")
