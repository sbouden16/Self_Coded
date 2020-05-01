import unittest
from BMI_Index_calculator import *


class Values(unittest.TestCase):
    heights = [1.4,1.74,1.76,1.85,1.92,1.45]
    weights = [85,76,101,67,100,96]
    res = BMI_Index_calculator()
    
    def testUnits(self):
        for i in self.heights:
            for j in self.weights:
                bmi = j/(i*i)
                self.assertEquals(self.res.Index_Calculator(i,j),bmi)
        
    def testNegatives(self):
        self.assertRaises(BadUnitError,self.res.Index_Calculator,1.7,-80)
    def testBigger_than_One(self):
        self.assertRaises(BadDataError,self.res.Index_Calculator,1.75,3)

if __name__ == "__main__":
    unittest.main()
