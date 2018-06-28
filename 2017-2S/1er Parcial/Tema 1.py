#Resuelto por Patricio González

################################### Ejercicio ###################################

#Datos del ejercicio
tareas = ["pintar soldados", "hornear galletas", "armar muñecos", "cortar papel de regalo"]

inicio = [678, 200, 240, 423]
duración = [300, 800, 456, 112]

#Para poder empezar a resolver, primero necesitaremos una lista que tenga cuando se finaliza
#cada una de las actividades, es decir al inicio debemos sumarle la duración, esta suma
#es más fácil hacerla teniendo estas listas como arreglos
import numpy as np

a_inicio=np.array(inicio)
a_duracion=np.array(duración)

a_finalizacion=a_inicio+a_duracion

#Ahora convertimos este arreglo a lista
finalizacion=list(a_finalizacion)   #También podemos usar la función .tolist()
                                    #finalizacion=a_finalizacion.tolist()

#Ahora que ya tenemos esto, nuestro criterio de búsqueda será comenzar por aquellas
#tareas que terminen más tarde, es decir iremos buscando las de mayor valor en la
#lista de finalización, además de esto la duración de todas las tareas no deberá
#exceder los 1440 minutos

#Dado que esto es un ciclo repetitivo basado en condiciones usaremos un ciclo while

#Primero creamos una lista donde añadiremos las tareas para posteriormente imprimirlas
#Y también iniciaremos un contador para saber cuantos minutos llevamos de duración

trabajos=[]
total=0

#El ciclo deberá repetirse mientras el total sea menor o igual 1440
while total<=1440:
    #Buscamos cual es la tarea que termina mas tarde
    latest=max(finalizacion)

    #Posteriormente buscamos su indice
    i_latest=finalizacion.index(latest)

    #Con este indice podemos acceder a la lista de tareas para saber a que tarea
    #Corresponde, y cuanto tiempo de duración tiene
    work=tareas[i_latest]
    time=duración[i_latest]

    #Ahora para poder buscar el siguiente valor máximo, lo que hacemos es al actual valor
    #Cambiarlo por otro número ( ya sea 0 o un número negativo), para que en la siguiente
    #Iteración ya no lo tome en consideración
    finalizacion[i_latest]=-1

    #Ahora añadimos la tarea a la lista, y sumamos el tiempo total
    total=total+time
    trabajos.append(work)

#Una vez que salimos del ciclo while ya tendremos lista las actividades, por lo que ya
#Podemos presentar por pantalla las tareas

print("+"+"-"*14+"+")
print("|Tareas del día|")
print("+"+"-"*14+"+")

#Iteramos sobre la lista de actividades, como en el ejemplo van numeradas las actividades
#Lo ideal sería iterar en función de un range para poder usar los indices como
#Numeradores
for i in range(len(trabajos)):
    print("%d. %s"%(i+1,trabajos[i].capitalize()))   #Ponemos i+1 porque i comienza en 0




#Durante una lección o examen no es recomendable declarar nombres de variables muy largas como
#algunas de las que declaré yo, pues se necesita mas tiempo para estar escribiendola a cada
#momento solo hago uso de nombres así para facilidad de comprensión :)