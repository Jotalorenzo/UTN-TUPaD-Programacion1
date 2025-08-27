#Ejercicio 8: menu

nombre: str = input("Ingrese su nombre: ")

print("1. Ingrese 1 para su nombre en mayusculas")
print("2. Ingrese 2 para su nombre en minusculas")
print("3. Ingrese 3 para su primera letra de su nombre en mayusculas")
numero: int = int(input("Ingrese un número de la lista anterior: "))

if numero == 1:
    print(nombre.upper())
elif numero == 2:
    print(nombre.lower())
elif numero == 3:
    print(nombre.title())
