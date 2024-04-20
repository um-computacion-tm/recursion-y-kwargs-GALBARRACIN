def factorial_iterativo(n):
    """Calcula el factorial de un número de manera iterativa.""" #Iteración significa repetir varias veces un proceso con la intención de alcanzar una meta deseada.
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

def factorial_recursivo(n):
    """Calcula el factorial de un número de manera recursiva.""" #Recurcion significa que contiene se a sí mismo un número indefinido de veces.
    if n == 0:
        return 1
    else:
        return n * factorial_recursivo(n - 1)

def test_factorial():
    """Realiza pruebas de los métodos de cálculo del factorial."""
    numeros = [0, 1, 5, 10]  # Números para los cuales se calculará el factorial
    for num in numeros:
        factorial_iterativo_resultado = factorial_iterativo(num)
        factorial_recursivo_resultado = factorial_recursivo(num)
        print(f"Factorial de {num} (Iterativo): {factorial_iterativo_resultado}")
        print(f"Factorial de {num} (Recursivo): {factorial_recursivo_resultado}")
        print()  # Salto de línea para separar resultados

# Llamamos a la función de prueba
test_factorial()