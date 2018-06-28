tareas = ["pintar soldados", "hornear galletas", "armar muñecos", "cortar papel de regalo"]

inicio = [678, 200, 240, 423]
duración = [300, 800, 456, 112]

import numpy as np

a_inicio=np.array(inicio)
a_duracion=np.array(duración)

a_finalizacion=a_inicio+a_duracion

finalizacion=list(a_finalizacion)  
trabajos=[]
total=0

while total<=1440:
    latest=max(finalizacion)
    i_latest=finalizacion.index(latest)

    work=tareas[i_latest]
    time=duración[i_latest]

    finalizacion[i_latest]=-1
    total=total+time
    trabajos.append(work)

print("+"+"-"*14+"+")
print("|Tareas del día|")
print("+"+"-"*14+"+")

for i in range(len(trabajos)):
    print("%d. %s"%(i+1,trabajos[i].capitalize()))
