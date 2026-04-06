'''
usando comandos logicos elif e or 
'''
print(f"\nDigite M para Masculino e F para Feminino: ")
genero =        (input("Genero 'M' ou 'F' => "))    # string
if  genero == "M" or genero == "m" :
    print(f"  => Masculino  ")
elif genero == "F" or genero == "f" :
    print(f"  => Masculino  ")
else:
    print(f"  => Genero invalido  ")
#
print(f"\nFim")
