import unittest

# Definición de la función fibonacci para calcular el número Fibonacci de un número n
def fibonacci(n): 
    # Caso base: si n es 0, devuelve 0
    if n == 0:
        return 0
    # Caso base: si n es 1, devuelve 1
    elif n == 1:
        return 1
        
    # Si n es mayor que 1, calcula el número Fibonacci recursivamente (osea que contiene a sí mismo un número indefinido de veces)
    resultado = fibonacci(n - 1) + fibonacci(n - 2)
    return resultado

# Definición de la clase TestFibonacci para realizar pruebas unitarias
class TestFibonacci(unittest.TestCase):
    # Prueba para verificar que fibonacci(0) devuelve 0
    def test_with_0(self):
        resultado = fibonacci(0)
        self.assertEqual(resultado, 0)

    # Prueba para verificar que fibonacci(1) devuelve 1
    def test_with_1(self):
        resultado = fibonacci(1)
        self.assertEqual(resultado, 1)

    # Prueba para verificar que fibonacci(2) devuelve 1
    def test_with_2(self):
        resultado = fibonacci(2)
        self.assertEqual(resultado, 1)

    # Prueba para verificar que fibonacci(3) devuelve 2
    def test_with_3(self):
        resultado = fibonacci(3)
        self.assertEqual(resultado, 2)

    # Sigo verificando con diferentes numeros

    def test_with_4(self):
        resultado = fibonacci(4)
        self.assertEqual(resultado, 4)

    def test_with_5(self):
        resultado = fibonacci(5)
        self.assertEqual(resultado, 5)

    def test_with_6(self):
        resultado = fibonacci(6)
        self.assertEqual(resultado, 8)

    def test_with_7(self):
        resultado = fibonacci(7)
        self.assertEqual(resultado, 13)

    def test_with_8(self):
        resultado = fibonacci(8)
        self.assertEqual(resultado, 21)

    def test_with_9(self):
        resultado = fibonacci(9)
        self.assertEqual(resultado, 34)

    def test_with_10(self):
        resultado = fibonacci(10)
        self.assertEqual(resultado, 55)

    def test_with_11(self):
        resultado = fibonacci(11)
        self.assertEqual(resultado, 89)

    def test_with_12(self):
        resultado = fibonacci(12)
        self.assertEqual(resultado, 144)

    def test_with_13(self):
        resultado = fibonacci(13)
        self.assertEqual(resultado, 233)

    def test_with_14(self):
        resultado = fibonacci(14)
        self.assertEqual(resultado, 377)

    def test_with_15(self):
        resultado = fibonacci(15)
        self.assertEqual(resultado, 610)

    def test_with_16(self):
        resultado = fibonacci(16)
        self.assertEqual(resultado, 987)

    # Y siguen las pruebas siguiendo la secuencia Fibonacci, me canse xd 
    # Ejecución de las pruebas unitarias al correr el script //ALBARRACIN
unittest.main()
