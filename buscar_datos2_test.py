import unittest

# Importamos la función buscar_datos y la base de datos simulada 'database' del módulo buscar_datos
from buscar_datos1 import buscar_datos, database

# Definimos una clase que hereda de unittest.TestCase para agrupar nuestras pruebas
class TestInDatabase(unittest.TestCase):

    # Definimos una prueba para buscar datos de una persona específica en la base de datos
    def test_individuo1(self):
        resultado = buscar_datos("Pablo", "Diego", "Ruiz", "Picasso", **database)
        self.assertEqual(resultado, ["individuo1"])  # Verificamos que el resultado sea el esperado

    def test_individuo2(self):
        resultado = buscar_datos("Valentina", "Sofia", "Jaramillo", "Ortiz", **database)
        self.assertEqual(resultado, ["individuo2"])
    
    def test_individuo3(self):
        resultado = buscar_datos("Valentina", "Valeria","Santilli","Rodriguez", **database)
        self.assertEqual(resultado, ["individuo3"])

    def test_individuo4(self):
        resultado = buscar_datos("Gonzalo", "Nahuel", "Albarracin", "Elias", **database)
        self.assertEqual(resultado, ["individuo4"])

    def test_individuo7(self):
        resultado = buscar_datos("Ana", "Isabel", "Garcia", "Lopez", **database)
        self.assertEqual(resultado, ["individuo7"])

    def test_individuo8(self):
        resultado = buscar_datos("Carlos", "Alberto", "Dominguez", "Fernandez", **database)
        self.assertEqual(resultado, ["individuo8"])

    def test_individuo9(self):
        resultado = buscar_datos("Elena", "Sofia", "Navarro", "Morales", **database)
        self.assertEqual(resultado, ["individuo9"])

    def test_individuo10(self):
        resultado = buscar_datos("Pedro", "Antonio", "Jimenez", "Ramos", **database)
        self.assertEqual(resultado, ["individuo10"])
    
    # Pruebas para buscar personas con nombres similares
    def test_individuos_iguales(self):
        resultado = buscar_datos("Valentina", **database)
        self.assertEqual(resultado, ["individuo2","individuo3"])

    # Prueba para buscar datos con nombres y apellidos mezclados
    def  test_datos_mezclados(self):      
        resultado = buscar_datos("Ruiz", "Pablo", "Picasso", "Diego", **database)
        self.assertEqual(resultado, ["individuo1"])

    # Prueba para buscar datos de una persona que no existe en la base de datos
    def  test_individuo_inexistente(self):      
        resultado = buscar_datos("Arturito", "Robertito", "Casimiro", "Matienzo", **database)
        self.assertEqual(resultado, " No se encuentra dentro de la base de datos")

    def  test_individuo_inexistente(self):      
        resultado = buscar_datos("Lujan", "Rooh", "Velazquez", "Ubuntu", **database)
        self.assertEqual(resultado, "No se encuentran dentro de la base de datos")

    def  test_individuo_inexistente(self):      
        resultado = buscar_datos("Melanie", "Nicole", "Venabidez", "Kali", **database)
        self.assertEqual(resultado, "No se encuentran dentro de la base de datos")

# Ejecutamos las pruebas
unittest.main()  