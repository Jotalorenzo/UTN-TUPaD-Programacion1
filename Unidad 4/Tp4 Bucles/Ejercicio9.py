'''
Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
poder procesar 100 números cambiando solo un valor).
'''

n :int = int(input("Ingrese la cantidad de numeros a promediar: "))
suma :int = 0

for i in range(n):
    num :int = int(input(f"Ingrese un numero {i+1}: "))
    suma += num

promedio :float = suma / n
print(f"El promedio de los {n} numeros es: {promedio}")

