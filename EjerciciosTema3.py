#Ejercicio 1
cadena1 = "escritorio"
print(cadena1[3])

#Ejercicio 2
cadena2 = "No es por nada, pero este videojuego es demasiado fácil"
print(cadena2.find("videojuego"))

#Ejercicio 3
cadena3 = "Tengo que asegurarme de comprobar el ejercicio para que no tenga errores"
print(cadena3.rfind("ejercicio"))

#Ejercicio 4
cadena4 = "Escribir código es fundamental para aprender programación"
print(cadena4[0:8])

#Ejercicio 5
cadena5 = "Python es uno de los lenguajes más populares de la actualidad"
print(cadena5[6::3])

#Ejercicio 6
cadena6 = "Si trabajas con ordenadores no tienes que aguantar discusiones ni bromas estúpidas, además de que no se comen tu comida"
print(cadena6[::-1])

#Ejercicio 7
cadena7 = "Con estos ejercicios voy a adquirir todo lo necesario para dominar la lógica de programación"
print(cadena7.upper())

#Ejercicio 8 
lista1 = ["Este", "curso", "me", "gusta"]
cadena8 = " ".join(lista1)
print(cadena8)

#Ejercicio 9
cadena9 = "No sé con cuál quedarme, si con el primero o con el segundo"

print(cadena9.replace("primero","Javascript").replace("segundo","Python"))

#Ejercicio 10 
cadena10 = "Mi jefe me ha mandado aprender Python para el trabajo, y estoy emocionado".__contains__("trabajo")

print(cadena10)

#Ejercicio 11
cadena11 = "Python"*11

print(cadena11)

#Ejercicio 12
cadena12 = "esternocleidomastoideo".__len__()

print(cadena12,"caracteres")

#Ejercicio 13
lista2 = ["Pizza","Pasta","Focaccia"] 
print(lista2)

#Ejercicio 14
lenguajes = ["Python", "Ruby", "PHP", "CSS"]
lenguajes.append("JavaScript")
print(lenguajes)

#Ejercicio 15
marca = ["Acer", "Samsung", "Xiaomi", "Apple", "Windows", "LG"]
eliminada = marca[5]
marca.pop(5)
print(marca)
print(eliminada)

#Ejercicio 16
diccionario1 = {"Nombre":"Davide","Apellido":"Giovannetti"}
print(diccionario1)

#Ejercicio 17
print(diccionario1.get("Apellido"))

#Ejercicio 18
diccionario2 = {"nombre": "Juan Carlos", "Apellido": "Fernández", "Edad": 28}
diccionario2.__setitem__("Pais","España")
print(diccionario2)

#Ejercicio 19
tupla_ejercicio19 = (3, 2, 4, 5, 1, 2, 6, 2, 3, 1, 5, 7, 2, 8, 9)
print(tupla_ejercicio19.count(3))

#Ejercicio 20
tupla_ejercicio20 = (1, 2, 3, 4, 5, 1, 2, 3, 4)
listaTupla = list(tupla_ejercicio20)
print(listaTupla)

#Ejercicio 21
tupla_ejercicio21 = ("Python", "Java", "PHP", "SQL", "JavaScript", "Django")
a, b, c, d, e, f = tupla_ejercicio21
print(b)

#Ejercicio 22 
set1 = {8, 10, "once", "doce"}
set2 = {"once", 4, 5}
sets = set1.union(set2)
print(sets)

#Ejercicio 23
loteria = {"Python", "Java", "SQL", "jQuery", "Git", "Github"}
loteria.pop()
print(loteria)

#Ejercicio 24
nombres = {"Juan", "Sonia", "Iván", "Mayte", "José Manuel", "Javi", "Miriam"}
nombres.add("Lorenzo")
print(nombres)

#Ejercicio 25
b = 10 < 4
print(b)

#Ejercicio 26
comprobacion = 19238 / 38 > 92*59
print(comprobacion)

#Ejercicio 27
comprobacion2 = 25**0.5 == 5
print(comprobacion2)

prueba = "123456789"
print(prueba.__len__())