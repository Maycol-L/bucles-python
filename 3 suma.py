num = 0 
sum = 0
while True:
    num = int(input("ingrese su numero positivo para ser sumado,(ingrese 0 para terminar la suma)"))
    if num == 0:
        break
    elif num > 0:
        sum += num
    else :
        print ("no se aceptan numeros negativos")
print(f"la suma de sus numeros es = {sum}")