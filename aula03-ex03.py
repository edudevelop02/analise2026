'''

'''
print(f"\nDigite 2 numeros quaisquer : \n")
num_A =  int(input("Numero A =>"))    # inteiro
num_B =  int(input("Numero B =>"))    # inteiro

#print(f"\nMedia das notas ==> {media} \n")
if  num_A > num_B :
    print(f"  =>Numero A {num_A} > {num_B} ")
else:
    if  num_B > num_A:
        print(f"  =>Numero B {num_B} > {num_A} ")
    else:
        print(f"  =>Numeros A {num_A} e B {num_B} sao iguais ")
#
print(f"\nFim")
