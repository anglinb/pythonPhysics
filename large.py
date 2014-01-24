import math
import sys

def createPoint(point1x,point1y):
    return [point1x,point1y]

def createPointWithCharge(point1x,point1y,charge):
    return [point1x,point1y,charge]

def addCharge(point,charge):
    point.insert(2,charge)
    return point


def addCharges(points,charge):
   for (i, point) in enumerate(points):
        points[i] = addCharge(point,charge)
   return points


def findVector(point1,point2):
    vectorx = point2[0] - point1[0]
    vectory = point2[1] - point1[1]
    return [vectorx,vectory]

def findMag(vector):
    return math.sqrt(vector[0]**2+vector[1]**2)

def findVectorAngle(vector):
    return math.atan(vector[1]/vector[0])

def findVectorAngleDegree(vector):
    return findVectorAngle(vector)*57.2957795

def findUnitVector(vector):
    mag     = findMag(vector)
    vector[0] = vector[0]/mag
    vector[1] = vector[1]/mag
    return vector

def findUnitVectorFromPoints(point1,point2):
    return findUnitVector(findVector(point1,point2));

def findField(point1,vector):
    k = 9*10**9
    mag     = findMag(vector)
    return k*point1[2]/(mag**2)

def findVectorWithFieldAndVector(vector,field):
    return [vector[0]*field,vector[1]*field]


def sumVectors(vector_list):
    total_vector = [0,0]
    for vector in vector_list:
        total_vector[0] += vector[0]
        total_vector[1] += vector[1]
    return total_vector

def findFieldVector(point,target_point):
    return findVectorWithFieldAndVector(findUnitVectorFromPoints(point,target_point),findField(point,findVector(point,target_point)))

def findFinalFieldVector(target_point,points):
    vector_list = []
    for point in points:
        vector_list.append(findFieldVector(point,target_point))
    return sumVectors(vector_list)

def findSquarePointsNoCharge(vertex,length):
    all_points = findSquarePointsNoChargeE(vertex,length)
    target_point = all_points.pop(0)
    return [target_point,all_points]


def findSquarePointsNoChargeE(vertex,length):
    #0-----1
    #|     |
    #|     |
    #3-----2
    mega_points = [
        [ [0,length]      ,[length,length] ,[length,0]      ,[0,0]],
        [ [length,length] ,[length,0]      ,[0,0]           ,[0,length]],
        [ [length,0]      ,[0,0]           ,[0,length]      ,[length,length]],
        [ [0,0]           ,[0,length]      ,[length,length] ,[length,0]]
        ]
    return mega_points[vertex]

def findSquareVector(vertex,length,charge):
    returned = findSquarePointsNoCharge(vertex,length)
    target_point = returned[0]
    points = returned[1]
    points = addCharges(points,charge)
    return findFinalFieldVector(target_point,points)


