import numpy as np

M = np.array(([24771906,18451280,78493,133538,18554394,13548964],
              [5477807839,7046108694,798122,21104851,1967543913,2034702069],
              [21900,45500,36,156,6700,12200],
              [262800,546000,430,1900,80000,12200]))

españa=['elrubiusOMG','VEGETA777']
ecuador=['enchufetvLIVE','Kreizivoy']
mexico=['Yuya','Werevertumorro']

#Nombres de usuarios de los youtubers con mayor rentabilidad en cada país. Tipo de dato de respuesta: lista de strings .
rentabilidad=M[3,:]/M[0,:]
rentaEspaña=rentabilidad[:len(españa)]
rentaEcuador=rentabilidad[len(españa):(len(españa)+len(ecuador))]
rentaMexico=rentabilidad[(len(españa)+len(ecuador)):]
posicionEs=rentaEspaña.argmax()
posicionEc=rentaEcuador.argmax()
posicionMx=rentaMexico.argmax()
y_rentaEs=españa[posicionEs]
y_rentaEc=ecuador[posicionEc]
y_rentaMx=mexico[posicionMx]
mayorRentabilidad=[y_rentaEs,y_rentaEc,y_rentaMx]

#El nombre del país del youtuber con la mayor rentabilidad . Tipo de dato de la respuesta: string
maxRentaEs=rentaEspaña[posicionEs]
maxRentaEc=rentaEcuador[posicionEc]
maxRentaMx=rentaMexico[posicionMx]
if maxRentaEs>maxRentaEc and maxRentaEs>maxRentaMx:
    paisMayorRentabilidad='España'
elif maxRentaEc>maxRentaEs and maxRentaEc>maxRentaMx:
    paisMayorRentabilidad='Ecuador'
else:
    paisMayorRentabilidad='Mexico'

#Cuántos youtubers de España tienen más suscriptores que el youtuber más popular de América (Ecuador y México). Tipo de dato de respuesta: valor entero .
youtubersEspaña=M[0,:len(españa)]
youtubersAmerica=M[0,len(españa):]
maxPopularAmerica=youtubersAmerica.max()
masPopularesEspaña=youtubersEspaña[youtubersEspaña>maxPopularAmerica]
numYoutubersEspañoles=len(masPopularesEspaña)

#El número promedio de reproducciones de los youtubers con más de 1’000,000 de suscriptores. Tipo de dato de respuesta: valor entero.
suscriptores=M[0,:]
reproducciones=M[1,:]
suscriptoresMillon=reproducciones[suscriptores>1000000]
promedioReproducciones=int(suscriptoresMillon.mean())

#Cuántos youtubers de Ecuador hay en cada categoría. La categoría se calcula en base a la siguiente tabla: Tipo de dato de respuesta: ndarray de enteros .
# rango                 categoria
#0.0 a 0.30                 3
#0.31 a 0.60                2
#>0.61                      1

categoria3=0
categoria2=0
categoria1=0
for renta in rentaEcuador:
    if renta<=0.3:
        categoria3+=1
    elif renta>0.3 and renta<=0.6:
        categoria2+=1
    elif renta>0.6:
        categoria1+=1
numCategoria=[categoria1,categoria2,categoria3]
arregloCategorias=np.array(numCategoria,int)

#El país que generó más ganancias anuales y el país que generó menos ganancias anuales. Luego muestre el siguiente mensaje reemplazando los datos apropiadamente:
gananciasEspaña=M[3,:len(españa)].sum()
gananciasEcuador=M[3,len(españa):len(españa+ecuador)].sum()
gananciasMexico=M[3,len(españa+ecuador):].sum()
paises=['España','Ecuador','Mexico']
ganancias=[gananciasEspaña,gananciasEcuador,gananciasMexico]
gananciaMax=max(ganancias)
gananciaMin=min(ganancias)
paisGananciaMax=paises[ganancias.index(gananciaMax)]
paisGananciaMin=paises[ganancias.index(gananciaMin)]
porcentaje=((gananciaMax-gananciaMin)/gananciaMin)*100
print(paisGananciaMax,"generó",porcentaje,"% más de ganancias que", paisGananciaMin)