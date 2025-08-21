# Ejercicio 1: Hola Mundo
    # print("¡Hola Mundo!")
# Ejercicio 2: Ingrese un usuario
    # print(f"Hola, {input('Ingrese su usuario: ')}!")
# Ejercicio 3: ingreso de datos
'''
# nombre = input("Ingrese su nombre: ")
# apellido = input("Ingrese su apellido: ")
# edad = input("Ingrese su edad: ")
# Pais = input("Ingrese su país: ")
# print(f"Hola, Soy {nombre} {apellido}, tengo {edad} años y soy de {Pais}.")
'''
# Ejercicio 4: radio de un circulo
"""
radio = float(input("Ingrese el radio del círculo: "))
area = 3.14 * radio ** 2
perimetro = 2 * 3.14 * radio
print(f"El área del círculo es: {area}")
print(f"El perímetro del círculo es: {perimetro}")
"""
# Ejercicio 5: cantidad de segundos
"""
segundos = int(input("Ingrese la cantidad de segundos: "))
horas = segundos // 3600
print(f"equivalencia: {horas} horas")
"""
# Ejercicio 6: tabla de multiplicar
"""
numero = int(input("Ingrese un número para mostrar su tabla de multiplicar: "))
for i in range(0, 11):
    print(f"{numero} x {i} = {numero * i}")
"""
# Ejercicio 7 : numeros enteros != 0
"""
numero_1 = int(input("Ingrese un número entero distinto de cero: "))
numero_2 = int(input("Ingrese otro número entero distinto de cero: "))
suma = numero_1 + numero_2
resta = numero_1 - numero_2
producto = numero_1 * numero_2
cociente = numero_1 / numero_2
print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Producto: {producto}")
print(f"Cociente: {cociente}")

"""
# Ejerciicio 8: Indice de masa corporal
"""
altura = float(input("Ingrese su altura en metros: "))
peso = float(input("Ingrese su peso en kilogramos: "))
imc = peso / (altura ** 2)
print(f"Su índice de masa corporal (IMC) es: {imc}")
"""
# Ejercicio 9: Equivalencia de temperatura
"""
Grados_Celsius = float(input("Ingrese la temperatura en grados Celsius: "))
Grados_Fahrenheit = (Grados_Celsius * 9/5) + 32
print(f"La temperatura en grados Fahrenheit es: {Grados_Fahrenheit}")
"""
# Ejercicio 10: Promedio de tres numeros
"""

numero_1 = float(input("Ingrese el primer número: "))
numero_2 = float(input("Ingrese el segundo número: "))
numero_3 = float(input("Ingrese el tercer número: "))
promedio = (numero_1 + numero_2 + numero_3) / 3
print(f"El promedio de los tres números es: {promedio}")

"""

ruta_archivo = "C:\Users\jorge\OneDrive\Desktop\UTN\Programacion I\notas"
print(ruta_archivo)


