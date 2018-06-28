import numpy as np
matriz=np.array([[ 50,0,0,160,0,50],[0,0,150,0,0,0],[0,10,20,0,50,0]])
empleados=['maria2','jose15','xavi7']
trabajo=['www.espol.edu.ec', 'www.inec.gob.ec','www.sri.gob.ec']

#Tiempo total de uso de Internet
tiempoTotalUso=matriz.sum()
print("El tiempo total del uso del internet fue de",tiempoTotalUso,"minutos")

#Tiempo total de uso de Internet por empleado
tiempoPorEmpleado=matriz.sum(axis=1)
for numEmpleado in range(len(empleados)):
    print(empleados[numEmpleado],"uso el internet por",tiempoPorEmpleado[numEmpleado],"minutos")

#Tiempo total de visita por sitio
tiempoPorSitio=matriz.sum(axis=0)
for numSitio in range(len(tiempoPorSitio)):
    print("Se gasto",tiempoPorSitio[numSitio],"minutos en el sitio n°",numSitio+1)

#Tiempo total de visita por sitio de trabajo
tiempoPorSitio=matriz.sum(axis=0)
for numSitio in range(len(trabajo)):
    print("Se gasto",tiempoPorSitio[numSitio],"minutos en ",trabajo[numSitio])

#El nombre del empleado que más tiempo ha pasado en sitios que no son de trabajo
tiempoNoTrabajo=matriz[:,len(trabajo):]
tiempoPorEmpleadoNT=tiempoNoTrabajo.sum(axis=1)
posicion=np.argmax(tiempoPorEmpleadoNT)
nombreEmpleado=empleados[posicion]
print("El nombre del empleado que mas tiempo ha gastado en sitios que no son de trabajo es:",nombreEmpleado)

#El sitio de trabajo que mas tiempo ha usado
tiempoTrabajo=matriz[:,:len(trabajo)]
tiempoPorSitioTrabajo=tiempoTrabajo.sum(axis=0)
posicion=np.argmax(tiempoPorSitioTrabajo)
sitio=trabajo[posicion]
print("El sitio de trabajo con mas minutos es:",sitio)

#Si el proveedor de Internet cobra un valor de 5 centavos por minuto de visita a los sitios de trabajo y el doble para los otros sitios . Calcule el total a pagar en dólares.
costoMinuto=0.05
minutosTrabajo=matriz[:,:len(trabajo)].sum()
minutosNoTrabajo=matriz[:,len(trabajo):].sum()
total=(minutosTrabajo*costoMinuto)+(minutosNoTrabajo*2*costoMinuto)
print("Se debe pagar $ %.2f"%total)

#Cuantos empleados han visitado cada sitio.
numVisitas=np.where(matriz>0,1,0)
visitas=numVisitas.sum(axis=0)
for numeroSitio in range(len(visitas)):
    print("Es sitio n°",numeroSitio+1,"fue visitado por",visitas[numeroSitio],"persona(s)")