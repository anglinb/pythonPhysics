import large
import math
#problems2.py

# 21.42
a = 5.7/100 #m
q = float("5.4e-6")

print "a: "+str(a)+"m"
print "q: "+str(q)+"C"

pointa = [2*a,a]
pointb = [a,a]

print "Point A"+str(pointa)
v = large.findFinalFieldVector(pointa,[[0,0,q],[4*a,0,q]])
print v
print large.findMag(v)
print large.findVectorAngleDegree(v)

print "-----------------"
print "Point B"+str(pointb)
v = large.findFinalFieldVector(pointb,[[0,0,q],[4*a,0,q]])
print v
print large.findMag(v)
print large.findVectorAngleDegree(v)
