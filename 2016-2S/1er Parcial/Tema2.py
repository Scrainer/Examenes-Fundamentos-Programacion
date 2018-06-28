import numpy as np

sur=["LosEsteros","Pradera","RiocentroSur"]
centro=["Bahía","Malecón2000","MalecónSalado"]
norte=["MallDelSol","CityMall","RiocentroNorte"]

futbol=["zapatos-Adidas","zapatos-Nike","rodilleras-Reebok"]
natación=["short-Nike","gafasPiscina-Swingo","aletas-Speedo"]

M=np.array(([11.76,5.28,12.05,3.76,8.69,4.45],
            [3.67,8.10,3.79,4.85,5.05,9.29],
            [9.94,6.20,3.83,10.82,0.68,10.92],
            [6.12,2.83,1.93,0.14,7.78,12.48],
            [8.94,7.69,0.38,8.40,11.99,4.31],
            [9.42,4.99,3.37,5.30,4.14,8.19],
            [4.00,0.32,1.27,3.07,8.92,10.91],
            [1.70,4.26,7.30,2.71,7.55,0.93],
            [1.84,1.28,6.93,2.94,12.85,5.03]))

total_futbol=np.sum(M[:,:len(futbol)])

total__natacion=np.sum(M[:,:len(futbol)])

if total__natacion==total_futbol:
    print("Iguales: %.2f"%total__natacion)  #Si son iguales podemos poner total de natación o de futbol
elif total__natacion>total_futbol:
    print("Natación tiene mas ventas: %.2f"%total__natacion)
elif total_futbol>total__natacion:
    print("Fútbol tiene mas ventas: %.2f"%total_futbol)




total_por_tiendas=np.sum(M,axis=1)
tiendas_todas=sur+centro+norte
indice_ventas_max=np.argmax(total_por_tiendas)
lugar_ventas_max = tiendas_todas[indice_ventas_max]
valor_ventas_max = total_por_tiendas[indice_ventas_max] #valores ventas max es un vector (lista*) por eso solo uso un indice para ubicar el valor
print("%s, con un monto de %.2f"%(lugar_ventas_max,valor_ventas_max))



ventas_norte=np.sum(M[len(centro)+len(sur):,:],axis=1)
indice_max_norte=np.argmax(ventas_norte)
tienda_max_norte=norte[indice_max_norte]
valor_max_norte=ventas_norte[indice_max_norte]
print("%s con %.2f"%(tienda_max_norte,valor_max_norte))



ventas_art_sur=np.sum(M[:len(sur),:],axis=0)
articulos_todos=futbol+natación
indice_art_sur=np.argmax(ventas_art_sur)
art_nombre=articulos_todos[indice_art_sur]
print("%s"%art_nombre)




articulos=[]
tienda=input("Ingrese el nombre de una tienda: ")
if tienda in tiendas_todas:
    indice_fila=tiendas_todas.index(tienda)
    ventas_tienda=M[indice_fila,:]  #Solo esa fila y todas las columnas
    for i in range(len(articulos_todos)):
        if ventas_tienda[i]>0:
            articulos.append(articulos_todos[i])
    cant_articulos=len(articulos)
    articulos_imprimir=", ".join(articulos)
    print("Tienda: %s"%tienda)
    print("Productos distinto vendidos: %d"%cant_articulos)
    print("Productos: %s"%articulos_imprimir)
else:
    print("Tienda no existente")



ventas_natacion=np.sum(M[:,len(futbol):],axis=1)
tiendas_ventas_nat=ventas_natacion[ventas_natacion>0]
numero_tiendas_venta=len(tiendas_ventas_nat)
porcentaje=(numero_tiendas_venta/len(tiendas_todas))*100
print("Porcentaje: %.2f%s"%(porcentaje,"%"))



promedio=M[:,:len(futbol)].mean()
print("Promedio de venta de productos de fútbol: %.2f"%promedio)