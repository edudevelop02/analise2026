'''
calcular percentual de um valor 
# '''

val1    =  float(input("\nDigite o valor      =>"))    # real Float
porc    =  float(input("\nDigite o percentual desconto =>"))    # real Float
#print(val1)

percent = (val1 * (porc / 100))
val_desc = val1 - percent
#
print(f"\nPercentual {porc}% = {percent} ")
print(f"\nCom desconto       = {val_desc} ")
