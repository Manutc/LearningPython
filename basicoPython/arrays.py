#Arrays
#Los Arrays pueden ser listas o tuplas, las listas se pueden modificar y no tienen tamanyo fijo, las listas no se pueden modificar y tienen un tamanyo fijo debido a esto

tupla = (1,"dos",True)
print tupla[0::]

lista = [2,"tres",True,["uno",10]]
implista = lista[1]
print implista

#ArraysDentroDeArrays
implista = lista[3][0]
print implista

#ModificarTuplasDentroDeListas
lista[3][0] = 7
implista = lista[3][0]
print implista

#SeleccionarZonasDelArray
implista = lista[0:3]
print implista

#SeleccionarZonasArraysSaltos
lista = [1,2,3,4,5,6,7,8,9]
implista = lista[0:8:2]
print implista
#Funcionamiento: [dondeEmpieza:dondeTermina:LosQueVaSaltando(ej:2 salta uno, imprimiendo uno si y uno no)]

#Modificaciones en las listas
implista = lista[0::]
print implista
lista[0:5] = [4]
implista = lista[0::]
print implista

#Con numeros negativos se empieza desde el final de la lista
print lista[-3]

#Diccionarios
print "------------------------------------"

#El funcionamiento de los diccionarios es como el de las Listas pero en vez de usar numeros para acceder a las casillas se usa una clave que se pone antes
#En los diccionarios se puede cambiar el contenido pero no las claves
#Los diccionarios no tienen sus claves ordenadas por lo que no se pueden imprimir todas como en las listas, es decir, no funcionaria lo de diccionario[0:3:1]
diccionario = {'clave1':[1,2,3,4],
				'clave2':True,
				7:"Venezuela"}

print diccionario["clave1"]
print diccionario["clave2"]
print diccionario[7]