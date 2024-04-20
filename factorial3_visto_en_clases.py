import unittest

def factorial(n):
    if n == 1:
        return 1
    resultado = n * factorial(n-1)
    return resultado

class TestFactorial(unittest.TestCase):
    def test_con_1(self):
        resultado = factorial(1)
        self.assertEqual(resultado, 1)
    
    def test_con_2(self):
        resultado = factorial(2)
        self.assertEqual(resultado, 2)
    
    def test_con_3(self):
        resultado = factorial(3)
        self.assertEqual(resultado, 6)
    
    def test_con_4(self):
        resultado = factorial(4)
        self.assertEqual(resultado, 24)
    
    def test_con_5(self):
        resultado = factorial(5)
        self.assertEqual(resultado, 120)
    
    def test_con_6(self):
        resultado = factorial(6)
        self.assertEqual(resultado, 720)
    
    def test_con_7(self):
        resultado = factorial(7)
        self.assertEqual(resultado, 5040)

    def test_con_8(self):
        resultado = factorial(8)
        self.assertEqual(resultado, 5760)

    def test_con_9(self):
        resultado = factorial(9)
        self.assertEqual(resultado, 7200)

    def test_con_10(self):
        resultado = factorial(10)
        self.assertEqual(resultado, 8640)

    def test_con_11(self):
        resultado = factorial(11)
        self.assertEqual(resultado, 10800)

    def test_con_12(self):
        resultado = factorial(12)
        self.assertEqual(resultado, 15120)    

unittest.main()