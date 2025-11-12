
while True:

    que = int(input("desea sumar(1), restar(2) o salir(3) :"))
    if que == 3:
        print("chao ")
        break
    elif que == 1:
        num1 = int(input("ingrese el primer numero a sumar : "))
        num2 = int(input("ingrese el segundo numero a sumar :"))
        suma = num1 + num2 
        print(f"la suma entre sus numeros es {suma}")
    elif que == 2:
        num1 = int(input("ingrese el primer numero a restar :"))
        num2 = int(input("ingrese el segundo numero a restar :"))
        rest = num1 - num2
        print(f"la resta entre sus numeros es = {rest}")
    else:
        print ("opcion no valida intentelo nuevamente :")