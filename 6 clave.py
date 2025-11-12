clave = str(input("ingrese su clave :"))

for i in range(1, 4):
    val = str (input("valide su clave :"))
    if val == clave:
        print ("su clave es correcta")
        break
    else:
        print(f"su clave es incorrecta, este es tu intento {i} de 3")
    if  i == 3:
        print("ya no hay mas intentos")