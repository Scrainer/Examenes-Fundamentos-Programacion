f = ["a","c","z","m","k"]
g = [3,4,5,6,5,7]
t = ""
for c in f:
    a = f.index(c)
    b= g[:a]
    t = t + (c*len(b))
print(t)

#------------------------------------------

import numpy as np
vector = np.array([1,5,6,6,5,2,1,3,7,9,0,0,1,4,8])
print(np.unique(vector[vector % 2 == 0]).size)
