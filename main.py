from calculadora import sumar, restar, multiplicar, dividir, raiz_cuadrada

def mostrar_menu():
    print("Operaciones disponibles:")
    print("1 - Sumar")
    print("2 - Restar")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("5 - Raíz cuadrada")

mostrar_menu()
opcion = input("Elija una opción (1-5): ")

if opcion in ['1', '2', '3', '4']:
    a = float(input("Ingrese el primer número: "))
    b = float(input("Ingrese el segundo número: "))

    if opcion == '1':
        print("Resultado:", sumar(a, b))
    elif opcion == '2':
        print("Resultado:", restar(a, b))
    elif opcion == '3':
        print("Resultado:", multiplicar(a, b))
    elif opcion == '4':
        print("Resultado:", dividir(a, b))

elif opcion == '5':
    x = float(input("Ingrese el número: "))
    print("Resultado:", raiz_cuadrada(x))
else:
    print("Opción no válida")
