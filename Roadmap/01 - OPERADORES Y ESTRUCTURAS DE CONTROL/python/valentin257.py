#Tipos de operadores en python
""" 
Existen varios tipos de operadores en python
Aritméticos, Reciben como entrada dos valores numericos y resuelven la operacion aritmética (sumas, restas, multiplicacion, division, division sin decimales, potencia y modulo)
y devuelven un valor numerico
"""
#ejemplo de division y potencia
altura = 1.75
peso = 65 
print("altura",altura,"metros")
print("peso",peso,"kilos")
print("Indice de masa corporal",peso/altura**2)
#ejemplo de resta
año_de_nacimiento = 1993
año_actual =2024
print("edad",año_actual-año_de_nacimiento,"años")
#ejemplo de suma
dedos_mano_derecha = 5
dedos_mano_izquierda = 4
print("dedos totales",dedos_mano_derecha+dedos_mano_izquierda)
#ejemplo de division
distancia = 60
tiempo = 0.5
print("distancia",distancia,"kilometros")
print("tiempo", tiempo,"horas")
print("velocidad",distancia/tiempo,"km/h")
velocidad =120
#ejemplo de multiplicacion
print("distancia recorrida en media hora",velocidad*tiempo,"kilometros")
#ejemplo de division entera y de modulo
"""supongamos que tenemos 3 manzanas para 2 personas
para calcular cuantas manzanas sobran luego de hacer la division vamos a utilizar la operacion modulo"""
manzanas = 7
personas = 2
print("manzanas",manzanas)
print("personas",personas)
print("cantidad de manzanas para cada uno:",manzanas//personas)
print("despues de repartir las manzanas sobraran",manzanas%personas,"manzana")
#ejemplo de potencia
dos_al_cubo = 2**3
print("dos al cubo es igual a",dos_al_cubo)
"""
Relacionales, reciben como entrada dos valores numericos y establecen la relacion entre ellos y devuelve un valor de true o false segun
sea la relacion entre los valores (mayor, menor, igual, mayor o igual, menor o igual o desigual)
"""
cien = 100
diez = 10
#ejemplos
print("es cien menor a diez?",cien<diez)
print("es cien mayor a diez?",cien>diez)
print("es cien igual a diez?",cien==diez)
print("es cien menor o igual a diez?", cien<=diez)
print("es cien mayor o igual a diez?", cien>=diez)
print("es cien desigual a diez?",cien!=diez)

#operadores bit a bit
#CONTINUARAAAA
