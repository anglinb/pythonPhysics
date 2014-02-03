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

def findDistance(point1,point2):
    return findMag(findVector(point1,point2))

def findPotential(points):
    k = 9.0*10**9
    electric_field = 0
    ll = len(points)
    for (i, point) in enumerate(points):
        for x in xrange(i+1,ll):
            # print str(point)+" plays "+str(points[x])
            electric_field = electric_field + k*point[2]*points[x][2]/findDistance(point,points[x])
    return electric_field


def findVoltage(target,points):
    k = 9.0*10**9
    voltage = 0
    ll = len(points)
    for (i, point) in enumerate(points):
        voltage = voltage + k*point[2]/findDistance(point,target)
    return voltage



class Point:

    def __init__(self, x, y, z = "na",charge = "na",l = False):
        self.cord = [x,y,z]
        # self.cord[0] = x
        # self.cord[1] = y
        # self.cord[2] = z
        if z == "na":
            self.type = "2d"
        elif l == True:
            self.type = "l"
        else:
            self.type = "3d"
        self.charge = charge
        

    def findVector(self, end_point):
        if(self.type != end_point.type):
            raise Exception('IncompatiblePointSpace')
        if(self.type == "2d"):
            vector = self.findVector2space(end_point)
        elif(self.type == "3d"):
            vector = self.findVector3space(end_point)
        else:
            vector = self.findVectorLspace(end_point)
        return vector

    def findVector3space(self,end_point):
        vector = [end_point.cord[0] - self.cord[0],
                  end_point.cord[1] - self.cord[1],
                  end_point.cord[2] - self.cord[2]
                  ]
        return vector

    def findVector2space(self,end_point):
        vector = [end_point.cord[0] - self.cord[0],
                  end_point.cord[1] - self.cord[1],
                  ]
        return vector

    def findVectorLspace(self,end_point):
        vector = [end_point.cord[0]+" - "+self.cord[0],
                  end_point.cord[1]+" - "+self.cord[1],
                  end_point.cord[2]+" - "+self.cord[2]
                  ]
        return vector

    def findPotentialLspace(self,points):
        field_strings = []
        ll = len(points)
        for (i, point) in enumerate(points):
            for x in xrange(i+1,ll):
                field_strings.append(' k*'+point.charge+'*'+points[x].charge+'/'+self.findMag(point.findVector(points[x])))
        return ' + '.join(field_strings)

    def findFieldLspace(self, target, points):
        #target = Point("0","x","0","na",True)
        vector_strings = []
        for point in points:
            vector_strings.append('')
        return ' + '.join(vector_strings)
    def findMag(self,vector):

        mag = self.findMagLspace(vector)
        return mag

    def findMagLspace(self, vector):
        return '( ('+vector[0]+')**(2) + ('+vector[1]+')**(2) + ('+vector[2]+')**(2) )**(.5)'


