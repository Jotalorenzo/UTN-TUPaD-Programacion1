'''
 Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
menor, pero debe estar preparado para procesar 100 números con un solo cambio).
'''

contador_pares :int= 0
contador_impares :int= 0
contador_positivos :int= 0
contador_negativos :int= 0
n :int= int(input("¿Cuántos números desea ingresar? (máximo 100): "))

for i in range(n):
    numero :int= int(input(f"Ingrese un numero entero ({i+1}/{n}): "))
    
    if numero % 2 == 0:
        contador_pares += 1
    else:
        contador_impares += 1
    
    if numero > 0:
        contador_positivos += 1
    elif numero < 0:
        contador_negativos += 1

print(f"Números pares: {contador_pares}")
print(f"Números impares: {contador_impares}")
print(f"Números positivos: {contador_positivos}")
print(f"Números negativos: {contador_negativos}")


