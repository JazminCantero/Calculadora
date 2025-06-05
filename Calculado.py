def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: división por cero"
    return a / b
import math

def raiz_cuadrada(x):
    if x < 0:
        return "Error: raíz de número negativo"
    return math.sqrt(x)
