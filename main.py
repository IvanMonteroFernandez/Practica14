from M04_Practica14A.books import book
from M04_Practica14A.cat import cat
import json
import textwrap

"""Crear una llista per a cada classe creada book y cat."""
books = [
    book("Don quijote","blanca",1735,"cervantes","anaya",1000),
    book("Libro1","negra",1284,"itamar","editorial1",2039),
    book("Libro2","rojo",1272,"ivan","editorial2",2831),
    book("Libro3","verde",1234,"roger","editorial3",2123),
    book("libro4","amarilla",1224,"pedro","editorial4",1567),
]
cats = [
    cat("verde",145,65,"raza1"),
    cat("rojo",15,53,"raza2"),
    cat("azul",23,54,"raza3"),
    cat("rojo",23,566,"raza4"),
    cat("negro",14,25,"raza5")
]
"""Convertir les llistes creadas en diccionaris."""
books_list = []
for b in books:
    books_list.append(b.to_dict())
"""También se podría haber puesto como:
books_list = [b.to_dict() for b in books]"""
cats_list = []
for c in cats:
    cats_list.append(c.to_dict())
""" También se podría haber escrito como:
cats_list = [c.to_dict() for c in cats]"""

"""Guardem les llistes en un objecte contenidor en format diccionari"""
data = { "books":books_list,"cats":cats_list}

"""Guardar l’objecte contenidor en un arxiu en format .json"""
with open("JSON.API/practica14b.json",'w') as file:
    json.dump(data, file)

print(data)
