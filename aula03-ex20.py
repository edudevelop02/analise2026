'''
 

'''
print(f"\nteste : \n")
mes =  input("Digite o nome do mes =>").lower()   
if  mes in ["dezenbro", "janeiro", "fevereiro"] :
    print("Verao")

elif  mes in ["março", "abril", "maio"] :
    print("Outono")

elif  mes in ["junho", "julho", "agosto"] :
    print("Inverno")

elif  mes in ["setembro", "outubro", "novembro"] :
    print("Primavera")

else:
    print(f"  => ({mes}) MES digitado invalido !  ")

print(f"\nFim programa")
