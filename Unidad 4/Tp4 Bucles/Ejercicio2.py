#Ejercicio2 : Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.

numero = int(input("Ingrese un número entero: "))

contador_digitos = 0

if numero == 0:
    contador_digitos = 1
else:
    while numero != 0:
        numero //= 10
        contador_digitos += 1
        print(numero)

print("El número tiene", contador_digitos, "dígitos.")

