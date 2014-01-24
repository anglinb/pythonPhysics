import large
import math
#problems.ph

#21.89

distance = .092
charge = float("6.8e-6")
sqV = large.findSquareVector(1,distance,charge)
#print sqV
print "distance: "+str(distance)
print "charge: "+str(charge)
print "magnitude of vector: "+str(large.findMag(sqV))
print "vector: "+str(sqV)
print 
print "---------------"

points = large.findSquarePointsNoChargeE(0,.092)
points = large.addCharges(points, float("7.2e-6"))

print large.findFinalFieldVector([.092*math.sqrt(2)/2,.092*math.sqrt(2)/2],points)
print .092*math.sqrt(2)/2
print "---------------"

sqV = large.findSquareVector(1,.1,float("4.45e-3"))
print sqV
print large.findMag(sqV)*float("4.45e-3")


# 21.42

a = 5.7/100 #m
q = float("5.4e-6")

print "a: "+str(a)+"m"
print "q: "+str(q)+"C"

v = large.findFinalFieldVector([a,a],[[0,0,q],[4*a,a,q]])
print v
print large.findMag(v)
