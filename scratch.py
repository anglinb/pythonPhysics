import large
from sympy import *
large.findPotential([[1,3,3],[1,2,3]])

point1 = large.Point("a","b","c","q",True)

point2 = large.Point("2*a","2*b","2*c","q",True)



# print point1.findVector(point2)

# print point1.findPotentialLspace([point1,point2])

points = [
		large.Point("0","l","0","q",True),
		large.Point("l","l","0","q",True),
		large.Point("l","0","0","q",True),
		large.Point("0","0","0","q",True),
		large.Point("0","0","l","q",True),
		large.Point("l","l","l","q",True),
		large.Point("l","0","l","q",True),
		large.Point("0","l","l","q",True)
		]
# print point1.findPotentialLspace(points)
l, q, k = symbols('l q k')
points = [
		# large.Point("0","l","0","q",True),
		# large.Point("l","l","0","q",True),
		# large.Point("l","0","0","q",True),
		# large.Point("0","0","0","q",True),
		large.Point(".5*l",".5*l","0","q",True)
		]
init_printing()
print point1.findPotentialLspace(points)
# print simplify(point1.findPotentialLspace(points))