from Calculado import sumar, restar, multiplicar, dividir

print("Calculadora simple en Python")
a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))
operacion = input("Ingrese la operación (+, -, *, /): ")

if operacion == '+':
    print("Resultado:", sumar(a, b))
elif operacion == '-':
    print("Resultado:", restar(a, b))
elif operacion == '*':
    print("Resultado:", multiplicar(a, b))
elif operacion == '/':
    print("Resultado:", dividir(a, b))
else:
    print("Operación no válida")
