# Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.

numero_usuario :int= int(input("Ingrese un número entero positivo: "))
suma :int= 0
for i in range(0, numero_usuario):
    suma += i

print(f"La suma de todos los números entre 0 y {numero_usuario} es: {suma}")