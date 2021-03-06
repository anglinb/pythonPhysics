import random
import unittest
import large

def listInt(points):
    for (i, point) in enumerate(points):
        points[i] = int(point)
    return points
def trunc(f, n):
    '''Truncates/pads a float f to n decimal places without rounding'''
    slen = len('%.*f' % (n, f))
    return float(str(f)[:slen])

class TestSequenceFunctions(unittest.TestCase):



    def test_point(self):
        self.assertEqual(large.createPoint(1,2),[1,2])

    def test_point_with_charge(self):
        self.assertEqual(large.createPointWithCharge(1,2,3),[1,2,3])

    def test_add_charge(self):
        self.assertEqual(large.addCharge(large.createPoint(1,2),3),[1,2,3])

    def test_add_charges(self):
        self.assertEqual(large.addCharges([[1,2],[3,4]],5),[[1,2,5],[3,4,5]])
        
    def test_find_mag(self):
        self.assertEqual(large.findMag([3,4]),5)

    def test_find_vector_angle(self):
        self.assertEqual(trunc(large.findVectorAngle([1,2]),5),1.10714);

    def test_find_vector_angle_degree(self):
        self.assertEqual(trunc(large.findVectorAngleDegree([1,2]),5),63.43494)

    def test_find_vector(self):
        self.assertEqual(large.findVector([1,2],[3,4]),[2,2])

    def test_find_unit_vector(self):
        self.assertEqual(large.findUnitVector([3,4]),[.6,.8])

    def test_find_unit_vector_from_points(self):
        self.assertEqual(large.findUnitVectorFromPoints([0,0],[3,4]),[.6,.8])

    def test_find_field(self):
        self.assertEqual(large.findField([1,2,2],[3,4]),float("7.2e8")) 

    def test_find_vector_with_field_and_vector(self):
        self.assertEqual(large.findVectorWithFieldAndVector([1,2],2),[2,4])

    def test_sum_vectors(self):
        self.assertEqual(large.sumVectors([[1,2],[3,4]]),[4,6])

    def test_find_field_vector(self):
        self.assertEqual(large.findFieldVector([0,0,5],[3,4]), [float("1.08e9"),float("1.44e9")])

    def test_final_field_vector(self):
        self.assertEqual(large.findFinalFieldVector([3,4],[[0,0,5],[0,0,5]]),[float("2.16e9"),float("2.88e9")])

    def test_find_square_point_no_charge(self):
        test_target_points = [[0,1],[1,1],[1,0],[0,0]]
        for x in range(0,3):
            returned = large.findSquarePointsNoCharge(x,1)
            self.assertEqual(returned[0],test_target_points[x])
            self.assertTrue(test_target_points[x] not in returned[1])
            self.assertTrue(len(returned[1]) == 3)

    def test_find_square_vector(self):
        self.assertEqual(listInt(large.findSquareVector(1,1.22,float("2.55e-6"))),[20870,20870])
    
    def test_find_distance(self):
        self.assertEqual(large.findDistance([0,0],[3,4]),5)

    def test_find_potential(self):
        self.assertEqual(large.findPotential([[0,0,1],[0,1,1]]),float("9e9"))

    def test_find_volate(self):
        self.assertEqual(large.findVoltage([0,1],[[0,0,1],[0,2,1]]),2*float("9e9"))

    def test_point_instance_no_z(self):
        point = large.Point(1,1)
        self.assertEqual(point.type,"2d")

    def test_point_instance_with_z(self):
        point = large.Point(1,1,2)
        self.assertEqual(point.type,"3d")

    def test_point_vector_3space(self):
        begin_point = large.Point(1,1,1)
        end_point = large.Point(5,2,1)
        self.assertEqual(begin_point.findVector(end_point),[4,1,0])

    def test_point_vector_incompatible(self):
        begin_point = large.Point(1,1)
        end_point = large.Point(1,2,2)
        self.assertRaises(Exception, begin_point.findVector, end_point)

    def test_virtual_point(self):
        point1 = large.Point("a","b","c","na",True)
        point2 = large.Point("2a","2b","2c","na",True)
        self.assertEqual(point1.findVector(point2),['2a - a','2b - b','2c - c'])

if __name__ == '__main__':
    unittest.main()
