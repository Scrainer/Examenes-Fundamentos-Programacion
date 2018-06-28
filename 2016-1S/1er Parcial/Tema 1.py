lista = ["www.espol.edu.ec","www.google.com","www.sri.gob.ec","www.fiec.espol.edu.ec","www.uess.edu.ec","www.FIEC.espol.edu.ec","www.fict.espol.edu.ec","www.fcnm.Espol.edu.ec","www.ucsg.edu.ec","www.Stanford.edu","www.harvard.edu","www.stanford.edu","www.UCSG.edu.ec","www.google.com.ec","www.facebook.com","www.opensource.org","www.educacionbc.edu.mx"]

universidades=[]
for sitio in lista:
    sitio=sitio.upper()
    listaSitio=sitio.split(".")
    if "EDU" in listaSitio:
        posicion=listaSitio.index("EDU")
        nombreUniversidad=listaSitio[posicion-1]
        if nombreUniversidad not in universidades:
            universidades.append(nombreUniversidad)
print("En la lista aparecen", len(universidades),"universidades:")
for i in range(len(universidades)):
    print("\t%d.) %s"%(i+1,universidades[i]))

universidadesEcuador=[]
for sitio in lista:
    sitio=sitio.upper()
    listaSitio=sitio.split(".")
    if "EDU" in listaSitio and "EC" in listaSitio:
        posicion=listaSitio.index("EDU")
        nombreUniversidad=listaSitio[posicion-1]
        if nombreUniversidad not in universidadesEcuador:
            universidadesEcuador.append(nombreUniversidad)
print("En la lista aparecen", len(universidadesEcuador),"universidades:")
for i in range(len(universidadesEcuador)):
    print("\t%d.) %s"%(i+1,universidadesEcuador[i]))

usuario=input("Ingrese el usuario: ")
universidad=input("Ingrese el nombre/sigla de la universidad: ")
correo=usuario+"@"+universidad.lower()+".edu.ec"
print('El correo electrónico del usuario es: \n\t%s'%correo)