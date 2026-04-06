'''
ler 3 numeros e ao final mostre qual e o maior entre os 3

'''
print(f"\nDigite a temperatura : \n")
temp_A =  float(input("Temp =>"))    # inteiro
if  temp_A  <= 18:
    print(f"  =>Esta frio a {temp_A} Graus ")

elif temp_A > 18 and temp_A <= 24:
    print(f"  =>Esta Normal a {temp_A} Graus ")

else:
#    if  temp_A > 25:
        print(f"  =>Esta CALOR a {temp_A} Graus ")
#    else:
#        print(f"  =>Esta Congelando a {temp_A} Graus ")

print(f"\nFim")
