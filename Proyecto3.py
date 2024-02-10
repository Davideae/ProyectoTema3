texto = input("Ingrese el texto a analizar: ")
letraA = input("Ingrese letra A ")
letraB = input("Ingrese letra B ")
letraC = input("Ingrese letra C ")

textoPreparado = texto.lower().strip()
print(f"Su letra {letraA} aparece en el texto esta cantidad de veces: ",textoPreparado.count(letraA))
print(f"Su letra {letraB} aparece en el texto esta cantidad de veces: ",textoPreparado.count(letraB))
print(f"Su letra {letraC} aparece en el texto esta cantidad de veces: ",textoPreparado.count(letraC))

lista = textoPreparado.split(" ")
print("Su texto tiene esta cantidad de palabras: ",lista.__len__())

print("La primera letra del texto es: ",textoPreparado[0])
print("La ultima letra del texto es : ",textoPreparado[textoPreparado.__len__()-1])

textoInvertido = texto[::-1]
print("El texto invertido: ",textoInvertido)
comprobacion = textoPreparado.__contains__("python")
print("La palabra Python se encuentra en el texto: ",comprobacion)