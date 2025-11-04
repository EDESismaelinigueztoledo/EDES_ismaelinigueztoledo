import os
def celsius_a_fahrenheit(celsius):
    #Convierte grados Celsius a Fahrenheit
    return (celsius * 9/5) + 32


def tabla_multiplicar(numero):
    #Muestra la tabla de multiplicar del número del 1 al 10
    print(f"\nTabla de multiplicar del {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")


def mostrar_menu():
    #Muestra el menú principal
    os.system("cls")
    print("\n=== MENÚ PRINCIPAL ===")
    print("1) Conversión de temperatura (Celsius → Fahrenheit)")
    print("2) Tabla de multiplicar")
    print("3) Salir")


def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-3): ")

        if opcion == "1":
            try:
                os.system("cls")
                celsius = float(input("Ingrese la temperatura en grados Celsius: "))
                fahrenheit = celsius_a_fahrenheit(celsius)
                print(f"{celsius}°C equivalen a {fahrenheit:.2f}°F")
                os.system("pause")
            except ValueError:
                print("Por favor, ingrese un número válido.")

        elif opcion == "2":
            try:
                os.system("cls")
                numero = int(input("Ingrese un número entero: "))
                tabla_multiplicar(numero)
                os.system("pause")
            except ValueError:
                print("Por favor, ingrese un número entero válido.")

        elif opcion == "3":
            os.system("cls")
            print("¡Hasta luego!")
            break

        else:
            os.system("cls")
            print("Opción no válida. Intente de nuevo.")


# Ejecutar el programa
if __name__ == "__main__":
    main()
