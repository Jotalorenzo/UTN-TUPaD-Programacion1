""" Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función
range.
"""

multiplos : list = []

for i in range(0,101,4):
    if i % 4 == 0 :
        multiplos.append(i)

print(multiplos)