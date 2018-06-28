L = [12,9,1,3,2,10,20,5]

import random as rd
suma = 0
while suma<=20:
    r1=rd.randrange(0,len(L))
    r2=rd.randrange(0,len(L))
    r3=rd.randrange(0,len(L))
    suma=L[r1]+L[r2]+L[r3]
print("Suma:",suma)

#-----------------------------------
stars = ["Potter", "Ron Weasley","Dumbledore","Hermione Granger","Hagrid","Voldemort"]
print(stars[-4:-2])
print(stars[3][0:stars[3].find(" ")]+stars[1][3:])