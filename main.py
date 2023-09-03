def mostrar_menu():
    print("Menú de Opciones:")
    print("1. Convertir de binario a decima")
    print("2. Convertir de decimal a binario")
    print("3. Realizar una multiplicacion")
    print("4. Realizar una division")
    print("5. Realizar una resta")
    print("6. Realizar una suma")
    print("7. Salir")

def realizar_accion1():
    print("Has seleccionado la acción 1.")
    numero_binario = input("Ingresa un número binario: ")

    try:
        numero_decimal = int(numero_binario, 2)
        print(f"El número binario {numero_binario} es igual a {numero_decimal} en decimal.")
    except ValueError:
        print("Entrada no válida. Asegúrate de ingresar un número binario válido (0s y 1s).")

def realizar_accion2():

    numero_decimal = int(input("Ingresa un número decimal: "))
    def decimal_a_binario(numero):
        if numero == 0:
            return '0'
        resultado = ''
        while numero > 0:
            residuo = numero % 2
            resultado = str(residuo) + resultado
            numero = numero // 2
        return resultado

    numero_binario = decimal_a_binario(numero_decimal)

    print(f"El número decimal {numero_decimal} es igual a {numero_binario} en binario.")


def realizar_accion3():
    print("Has seleccionado la acción 3.")
    numero1 = 5
    numero2 = 100
    resultado = numero1 * numero2
    print(resultado)


def realizar_accion4():
    print("Has seleccionado la acción 4.")
    numero1 = 5000
    numero2 = 900
    resultado = numero1 / numero2
    print(resultado)

def realizar_accion5():
    print("Has seleccionado la acción 5.")
    numero1 = 9000
    numero2 = 5
    resultado = numero1 - numero2
    print(resultado)


def realizar_accion6():
        print("Has seleccionado la acción 6.")
        numero1 = 60
        numero2 = 5
        resultado = numero1 + numero2
        print(resultado)

def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1/2/3/4/5/6/7): ")

        if opcion == "1":
            realizar_accion1()
        elif opcion == "2":
            realizar_accion2()
        elif opcion == "3":
            realizar_accion3()
        elif opcion == "4":
            realizar_accion4()
        elif opcion == "5":
            realizar_accion5()
        elif opcion == "6":
            realizar_accion6()
        elif opcion == "7":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción válida (1/2/3/4/5/6/7).")

if __name__ == "__main__":
    main()


