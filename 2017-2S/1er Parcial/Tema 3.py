import numpy as np
m = np.array(([239034,678493,896321,32438,554213],
              [4568321,6745634,9754008,3242342,3456123],
              [234773,56743,123678,4783,90874],
              [45672,45212,90781,3904,90431]))
tipoGasolina = np.array(["Regular","Extra","Super","Premium"])
gasolineras = np.array(["Primax Alborada","PS Los Ríos","Mobil Cumbayá","Lutexsa CIA Ltda","PS Remigio Crespo"])
distrito =  np.array(["distrito1","distrito2","distrito1","distrito2","distrito4"])
ciudades = np.array(["Guayaquil","Babahoyo","Quito","Guayaquil","Cuenca"])

#1.
#gasolina_ingresada = input("Ingrese un tipo de gasolina: ")
#fila_gasolina=list(tipoGasolina).index(gasolina_ingresada)
#promedio=m[fila_gasolina,:].mean()
#locales=np.where(m[fila_gasolina,:]>promedio)
#print(gasolineras[locales])

#2.
##ciudad_ingresada = input("Ingrese una ciudad: ")
##gasolineras_ciudad = m.sum(axis=0)
##ciudad=np.where(ciudades==ciudad_ingresada)
##gasolineras_ciudad2 = gasolineras_ciudad[ciudad]
##conteo = np.where(gasolineras_ciudad2>15000000,1,0).sum()
##print(conteo)

#3
#fila_gasolina=list(tipoGasolina).index("Premium")
#gasolinaEscogida = m[fila_gasolina,:]
#posCiudad = np.where(distrito=="distrito1")
#ciudadesDistrito1=ciudades[posCiudad]
#gasolinaDistrito1=gasolinaEscogida[posCiudad]
#mayorGasolina = gasolinaDistrito1.argmax()
#print(ciudadesDistrito1[mayorGasolina])