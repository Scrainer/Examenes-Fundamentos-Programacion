import numpy as np
visitados=['maria2|www.facebook.com|160','xavi7|www.eluniverso.com|50','jose15|www.sri.gob.ec|30','maria2|www.twitter.com|30','xavi7|www.inec.gob.ec|10','maria2|www.espol.edu.ec|50','jose15|www.sri.gob.ec|120','xavi7|www.sri.gob.ec|20','maria2|www.twitter.com|20' ]
empleados=['maria2','jose15','xavi7']
trabajo=['www.espol.edu.ec', 'www.inec.gob.ec','www.sri.gob.ec']

noTrabajo=[]
for info in visitados:
    datos=info.split("|")
    sitio=datos[1]
    if sitio not in trabajo and sitio not in noTrabajo:
        noTrabajo.append(sitio)
print("Los sitios que no son de trabajo son: ",noTrabajo)

sitios=trabajo+noTrabajo
filas=len(empleados)
columnas=len(sitios)
tabulacion=np.zeros((filas,columnas),int)
for info in visitados:
    datos=info.split("|")
    usuario=datos[0]
    pagina=datos[1]
    minutos=int(datos[2])
    fila=empleados.index(usuario)
    columna=sitios.index(pagina)
    tabulacion[fila,columna]+=minutos
print(tabulacion)
