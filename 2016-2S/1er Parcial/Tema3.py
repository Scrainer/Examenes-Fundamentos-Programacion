transacciones = [ 'centro|Bahia|futbol|zapatos-Adidas|290.78|25-03-2013','centro|Malecon2000|natacion|chaleco-Fins|110.92|01-02-2014',
                  'sur|MallDelSur|natacion|gafasPiscina-Swingo|90.07|13-05-2014','centro|Bahia|natacion|zapatos-Nike|315.72|13-12-2015',
                  'norte|CityMall|natacion|gafasPiscina-Adidas|310.19|31-05-2016']


sur=[]
centro=[]
norte=[]
for info in transacciones:
    l_datos=info.split("|")
    sector=l_datos[0]
    tienda=l_datos[1]
    if sector=="sur" and (tienda not in sur):
        sur.append(tienda)
    elif sector=="centro" and (tienda not in centro):
        centro.append(tienda)
    elif sector=="norte" and (tienda not in norte):
        norte.append(tienda)
print("Sur:",sur)
print("Centro:",centro)
print("Norte:",norte)




año_usu=input("Ingrese año a consultar ventas: ")
total=0
for info in transacciones:
    l_datos=info.split("|")
    producto=l_datos[3]
    l_producto=producto.split("-")
    marca=l_producto[1]
    fecha=l_datos[-1]
    l_fecha=fecha.split("-")
    año=l_fecha[-1]
    mes=l_fecha[1]
    if marca=="Adidas" and año_usu==año and mes=="05":
        ventas=l_datos[-2]
        total=total+float(ventas)
print("El total de ventas de productos Adidas en el mes de mayo del año %s es: %.2f"%(año_usu,total))
