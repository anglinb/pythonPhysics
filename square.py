import math

k = 9*10**9 #k

distance = 1.22 #meters
charge = 2.55*10**-6 #C


vert = (k*charge)/(distance**2)
print vert


bottom = ((math.sqrt(2)/2)*k*charge)/((distance*math.sqrt(2))**2)

# bottom = math.sqrt(2)/2*k*charge/

print bottom