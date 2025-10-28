def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius} grados Celsius son {fahrenheit} grados Fahrenheit.")

celsius = int(input("Ingrese la temperatura en grados Celsius: "))

fahrenheit = celsius_a_fahrenheit(celsius)
