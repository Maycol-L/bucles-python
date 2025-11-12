num = float(input("ingresa tu numero :"))
invertido = 0
while num != 0:
    digito = num%10
    invertido = invertido*10+digito
    num = num // 10 
invertido = int(invertido)
print(invertido)
