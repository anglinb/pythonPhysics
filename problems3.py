#prolems3.py
import large
print "23.71---------------------"
print -1*large.findPotential([
	[0,0,float('33e-6')],
	[.36,0,float('33e-6')],
	[.12,0,float('-1.5e-6')] #point a
	]) + large.findPotential([
	[0,0,float('33e-6')],
	[.36,0,float('33e-6')],
	[.12,.14,float('-1.5e-6')] #point b
	])

print large.findPotential([
	[0,0,float('33e-6')],
	[.36,0,float('33e-6')],
	[.12,0,float('-1.5e-6')] #point a
	])