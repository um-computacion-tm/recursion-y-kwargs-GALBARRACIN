'''Solicita al usuario un número para calcular su factorial // ALBARRACIN'''
    # Definición de una función para calcular el factorial de un número de manera iterativa
def factorial_iterativo(n):
    resultado = 1  # Inicializamos el resultado en 1, ya que 0! = 1
    for i in range(1, n + 1):  # Recorremos desde 1 hasta n (inclusive)
        resultado *= i  # Multiplicamos el resultado por cada número en el rango
    return resultado  # Devolvemos el resultado del factorial

# Solicitamos al usuario que ingrese un número para calcular su factorial
numero = int(input("Ingresa un número para calcular su factorial: "))

# Verificamos si el número ingresado es negativo
if numero < 0:
    print("El factorial no está definido para números negativos.")
elif numero == 0:  # Si el número es 0, su factorial es 1
    print("El factorial de 0 es 1.")
else:  # En caso contrario, calculamos el factorial usando la función factorial_iterativo
    resultado_factorial = factorial_iterativo(numero)
    print(f"El factorial de {numero} es {resultado_factorial}.")  # Mostramos el resultado del factorial