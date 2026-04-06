'''
ler 3 numeros e ao final mostre qual e o maior entre os 3

'''
print(f"\nDigite 3 numeros quaisquer : \n")
num_A =  int(input("Numero A =>"))    # inteiro
num_B =  int(input("Numero B =>"))    # inteiro
num_C =  int(input("Numero C =>"))    # inteiro
#print(f"\nMedia das notas ==> {media} \n")
if  num_A > num_B and num_A > num_C:
    print(f"  =>Numero A {num_A} é o Maior numero ")
elif num_B > num_A and num_B > num_C:
    print(f"  =>Numero B {num_B} é o Maior numero ")
else:
    print(f"  =>Numero C {num_C} é o Maior numero ")
#
#elif   print(f"  =>Numero A B e C sao iguai ")        
#
print(f"\nFim")
