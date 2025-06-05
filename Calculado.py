def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b
def dividir(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: no se puede dividir por cero"
