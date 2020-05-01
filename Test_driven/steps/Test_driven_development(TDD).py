import unittest2
from roman_converter import *


class Values(unittest2.TestCase):
    listval = ((1, "I"), (35, "XXXV"), (10, "X"), (149, "CXLIX"), (1110,"MCX"))
    listnaturalnum = list(range(1,100,5))
    conv = converter()
    def testtoRomanconvert(self):
       """checking the correctness of conversion"""
       for a,b in self.listval:

           self.assertEqual(self.conv.convert_int_to_roman(a),b)
    def testtoIntconvert(self):
        for a,b in self.listval:
            self.assertEqual(self.conv.convert_roman_to_int(b),a)
    def testInferiorLimit(self):
        '''You call instance of another class (converter) and save it as as
        an attribute of Values Class and then you can use it in test '''
        self.assertRaises(OutOfRangeError,self.conv.convert_int_to_roman,0)
    def testSuperiorLimit(self):
        self.assertRaises(OutOfRangeError,self.conv.convert_int_to_roman,4000)
    def testNaturalNumb(self):          
        pass
        #for a in self.listnaturalnum:
            #self.assertEqual()
    def testUppercase(self):
        self.assertRaises(RomanNumberError,self.conv.convert_roman_to_int,"v")
    def testFraction(self):
        self.assertRaises(NumberInputError,self.conv.convert_int_to_roman,1.3)
    def testNegative(self):
        self.assertRaises(OutOfRangeError,self.conv.convert_int_to_roman,-1)

    def testIntToRoman_RomanToInteger(self):
        for a, b in self.listval:
            Int_to_Roman = self.conv.convert_int_to_roman(a)
            Roman_to_Int = self.conv.convert_roman_to_int(Int_to_Roman)
            self.assertEqual(Roman_to_Int, a)
    def testToMuchCaracters(self):
        self.assertRaises(RomanNumberError,
                          self.conv.convert_roman_to_int, "MMMMM")

        
    def correctRomanStart(self):
        pass

if __name__=="__main__":
    unittest2.main()

""" write the method that makes this test pass"""

""" do they do use cases diagrams""" #Tehy dont use it

""" write a test to check roman to integer"""

""" write more test to not exceed the range the roman numbers have"""
""" write test to check if the aplication works for all natural numbers from 1 to 4000"""

""" test for uppercases and fractions of numbers """

""" test that when you combert Int to Roman, and then again this roman result into INT, it has to be the same"""

""" test a roman number not to be repeated with to much caracters (Same caracters like MMMMM)"""
"""" test roman number can only beggin with some selected caracters"""

""" test for UEFA champion"""

""" write BMI index calculator with respect to TDD and BDD philosophy Note: no negative, and bigger always than 1"""

""" write a bunch of descriptive statistics measures using TDD philosophy:
 calculation of arithmetic mean, windsor mean, variance, standard deviation
quartiles""" 

""" run the rest of operatio  for calculator BDD"""


"make search og login gmail"
"make search that a searched item is found" "make sure that this works and send you where wanted"