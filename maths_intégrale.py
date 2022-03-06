"""
maths_integrale
"""

import math

n = int(input())
u = math.exp(1) - 1

for i in range(n):
    u = u * (i + 1) - 1

print(u)



from math import exp
from scipy.integrate import quad

xmin = 0.0
xmax = 1.0 

n = int(input("Entrez le rang"))
print(n)
def function(x):  
    return exp(x)*(1-x)**n

res = quad(function, xmin, xmax) 
print ('le resultat est : ', res)