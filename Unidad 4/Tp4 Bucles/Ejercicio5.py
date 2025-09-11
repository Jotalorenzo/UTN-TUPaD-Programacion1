# ) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random

numero_aleatorio :int= random.randint(0, 9)
intentos :int= 0
adivinado :int= True

while adivinado:
    numero_usuario = int(input("Adivina un número entre 0 y 9: "))
    intentos += 1
    if numero_usuario == numero_aleatorio:
        adivinado = False
        print(f"Has adivinado el número {numero_aleatorio} en {intentos} intentos.")
    else:
        print("Número incorrecto. Intenta de nuevo.")

