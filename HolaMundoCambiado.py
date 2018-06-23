#encoding: utf-8
print ("Inicia programa")
a=3
e=5
r=0.568
cientific=0.56e4

print (e)
print (r)
print (cientific)

#Comentarios
print ("Operaciones")
print (e+r)
print (r-e)
print (e*e)
print (a**3)

print(a/e)

#Cadenas 

cadena='Texto1 \n Con caracter de escape '
cadenas='Texto2'
cadenat="""Cadena con saltos
Linea 2
Linea 3
"""
cadenota="Cadenita" * 4
print (cadena)
print (cadenas)
print (cadenat)
print (type(cadena))
print (type(cadenas))

print (cadenota)

#Concatenacion
cadenacc=cadena+cadena
print (cadenacc)

bT=True
bF=False

bAnd= bT and bF
print (bAnd)

#Listas
lista1=[a,e,cientific,[cadena,cadenas],bAnd]
print (lista1)

l1_4= lista1[3][1]
print (l1_4)


#Diccionarios

dicci={'Clave1':553423,'Clave2':[1,2,3],'Clave3':'Gato'}
print(dicci['Clave2'])
datoD = dicci['Clave2']
print (datoD[2])
