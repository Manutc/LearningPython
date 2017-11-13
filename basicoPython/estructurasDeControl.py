#If
#En python al no usar corchetes funciona por bloques, en los que se mantiene o se saca con la tabulacion, de igual forma el else que corresponde a cada if es el que este a su altura de tabulacion
#En python else if se escribe como elif
edad = 19
mayoriaEdad = 18

if edad >= 0 and edad < mayoriaEdad:
	print "Eres menor de edad"
	print "Esto es dentro del if al tabular"
elif edad >=18 and edad < 30:
	print "Eres una persona joven"
else:
	print "No eres tan joven"

print "Eso es fuera del if al no tabular"

#Bucles
#While
i=0;

while i < 10 :
	
	if i == 4:
		break

	if i == 2:
		i = i + 1
		continue

	
	print "Contador while: " +str(i)
	i = i + 1

#For
#El for se puede usar incluso como lector de caracteres

for i in "Hola":
	print i

#Se puede usar para leer listas
lista = ["Elemento1", "Elemento2", "Elemento3"]

for i in lista:
	print i

#Se puede usar de la forma clasica
for i in range(3):
	print "Buenas" +str(i)