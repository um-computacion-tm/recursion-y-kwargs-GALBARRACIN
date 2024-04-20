import unittest

def buscar_datos(*args, **kwargs):
    arg_set = set(args)  # Conjunto que contiene los valores pasados a la función a través de argumentos.
    listado_personas = []  # Lista para almacenar las personas cuyos datos coinciden con los datos buscados.

    for persona, datos in kwargs.items():
        datos_set = set(datos.values())  # Conjunto de los valores del diccionario de cada persona.

        if arg_set.issubset(datos_set):  # Verifica si los valores de los argumentos pasados son subconjunto de los datos contenidos en database.
            listado_personas.append(persona)  # Agrega las personas que coinciden a la lista.

    if listado_personas:
        return listado_personas  # Devuelve las personas que coinciden con los datos buscados.
    else:
        return "No se encuentran dentro de la base de datos"  # Devuelve un mensaje si no se encuentra ninguna coincidencia.

# Base de datos con personas y sus datos.
database = {
    "individuo1": {
        "primer_nombre": "Pablo",
        "segundo_nombre": "Diego",
        "primer_apellido": "Ruiz",
        "segundo_apellido": "Picasso"
    },
    "individuo2": {
        "primer_nombre": "Valentina",
        "segundo_nombre": "Sofia",
        "primer_apellido": "Jaramillo",
        "segundo_apellido": "Ortiz"
    },
    "individuo3": {
        "primer_nombre": "Valentina", # Valentina volve :( ahre
        "segundo_nombre": "Valeria",
        "primer_apellido": "Santilli", 
        "segundo_apellido": "Rodriguez"
    },
    "individuo4": {
        "primer_nombre": "Gonzalo", # Yo jiji
        "segundo_nombre": "Nahuel",
        "primer_apellido": "Albarracin",
        "segundo_apellido": "Elias" #?
    },
    "individuo5": {
        "primer_nombre": "Maria",
        "segundo_nombre": "Luisa",
        "primer_apellido": "Rodriguez",
        "segundo_apellido": "Gomez"
    },
    "individuo6": {
        "primer_nombre": "Luis",
        "segundo_nombre": "Miguel",
        "primer_apellido": "Martinez",
        "segundo_apellido": "Hernandez"
    },
    "individuo7": {
        "primer_nombre": "Ana",
        "segundo_nombre": "Isabel",
        "primer_apellido": "Garcia",
        "segundo_apellido": "Lopez"
    },
    "individuo8": {
        "primer_nombre": "Carlos",
        "segundo_nombre": "Alberto",
        "primer_apellido": "Dominguez",
        "segundo_apellido": "Fernandez"
    },
    "individuo9": {
        "primer_nombre": "Elena",
        "segundo_nombre": "Sofia",
        "primer_apellido": "Navarro",
        "segundo_apellido": "Morales"
    },
    "individuo10": {
        "primer_nombre": "Pedro",
        "segundo_nombre": "Antonio",
        "primer_apellido": "Jimenez",
        "segundo_apellido": "Ramos"
    }
}

# Llamada a la función para buscar datos específicos en la base de datos.
resultado = buscar_datos("Pablo", "Diego", "Ruiz", "Picasso", **database)
print("Key:", resultado)

# Prueba unitaria para verificar el funcionamiento de la función.
if __name__ == "__main__":
    unittest.main()