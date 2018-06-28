print("Literal a")


mensaje = "No basta saber, se debe también aplicar. No es suficiente querer, se debe también hacer. Goethe (1749-1832)"
largo=len(mensaje)
cual='be'
cuantos=0
lista=[]
donde=1
i=0

#Esto no es parte del ejercicio####################
print("%-7s|%-5s|%s"%("cuantos","donde","lista")) #
print("%-7d|%-5d|%s" % (cuantos, donde, lista))   #
###################################################

while (i<largo):
    donde=mensaje[i:].find(cual)
    if (donde>0):
        cuantos=cuantos+1
        i=i+donde+1
        lista.append(donde)
    else:
        i=i+1

    #Esto no es parte del ejercicio#################
    print("%-7d|%-5d|%s" % (cuantos, donde, lista))#
    ################################################

print("Hasta aquí es la prueba de escritorio")
print (cuantos)
print (lista)

#Se puede observar que después de las sexta iteración se repite lo mismo, así que no se preocupen, no era necesario repetirlo
#tantas veces como se imprime en el codigo