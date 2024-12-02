None
diccionario = {
    "chuchinga" : "persona cobarde",
    "badulaque" : "inutil",
    "guagua" : "niño-a",
    "achichay" : "expresion ante el frio",
    "chumado" : "persona hebria",
    "urcunina" : "volcan galeras",
    "verraco" : "persona dura de tratar o que hace un gran esfuerzo"
}
for i in range(3):
    palabra = input("escribe la palabra que no entiendas (en minusculas):")
    if palabra in diccionario.keys():
            print(diccionario[palabra])
    else:
        print("esta palabra no esta en el diccionario")
