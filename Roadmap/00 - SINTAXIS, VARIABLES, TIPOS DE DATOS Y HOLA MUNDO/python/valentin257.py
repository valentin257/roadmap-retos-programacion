#Esto es un comentario
#https://python.org
#En python se puede crear comentarios con el simbolo numeral
""" Tambien se pueden crear comentarios
de varias lineas utilizando tres comillas dobles
"""
'''
Tambien se pueden crear comentarios utilizando tres comillas
simples
'''
"""
Variables.
se escriben escribiendo el nombre de la variable en minusculas seguido de un espacio, un signo igual, espacio y el valor asignado a la variable
"""
variable_1 = 1
variable_2 = "mocos"
print(variable_2)
#el valor de las variables puede cambiar segun avanzamos 
variable_2 = "macaco"
print(variable_2)
"""
Constantes.
Python no tiene constantes, todo puede ser variable,
una constanste puede representarse en mayusculas
"""
CONSTANTE = "color azul"
print(CONSTANTE)
""" si bien la constante puede variar si se le asigna un nuevo valor, queda por conveniencia 
que no se puede modificar
"""
CONSTANTE = "verde"
print(CONSTANTE)
#Tipos de datos primitivos en python
#Enteros (INT), para representar numeros enteros
edad = 31
#Flotantes (Float), para representar numeros con coma o expresiones decimales
altura = 1,73
#Booleanos (bool), para representar valores binarios de verdadero o falso (True o False)
soy_guapo = True
tengo_hambre = False
#Strings o Cadenas de texto (str), para representar textos, se escriben entre comillas
nombre = "valentin"
pasatiempos = """ Escuchar musica
correr
pintar
sacarme los mocos
"""
print("nombre",nombre)
print ("edad",edad)
print("altura",altura)
print("soy guapo?",soy_guapo)
print("tengo hammbre?",tengo_hambre)
print("pasatiempos",pasatiempos)
print("¡Hola Python!")
