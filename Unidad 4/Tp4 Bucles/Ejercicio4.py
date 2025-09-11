# Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0.
numero : int = -1
resultado : int = 0
while numero != 0:
    numero : int = int(input("Ingrese un numero (0 para salir) "))
    resultado : int = resultado + numero

print(f"El total acumulado es {resultado}")