# Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.

numero1 : int = int(input("Ingrese un numero "))
numero2 : int = int(input("Ingrese otro numero "))

resultado : int = 0
if numero1 > numero2:
    aux = numero2
    numero2 = numero1
    numero1 = aux

for i in range(numero1+1,numero2):
    resultado = i + resultado

print(f"La suma de los numeros entre {numero1} y {numero2} es {resultado}")