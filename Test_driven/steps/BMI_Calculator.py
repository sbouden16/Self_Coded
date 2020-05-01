class BadUnitError(Exception):
    pass
class BadDataError(Exception):
    pass
class BMI_Index():
    def Index_Calculator(self,height,weight):
        bmi = weight/(height*height)
        if bmi > 1:
            if bmi <= 18.5:
                #print("Your BMI is", bmi, "which means you are underweight.")
                return bmi
            elif bmi > 18.5 and bmi < 25:
                #print("Your BMI is", bmi, "which means you are normal.")
                return bmi
            elif bmi > 25 and bmi < 30:
                #print("your BMI is", bmi, "overweight.")
                return bmi

            elif bmi > 30:
                #print("Your BMI is", bmi, "which means you are obese.")
                return bmi
        else:
            if bmi > 0 and bmi <= 1:
                raise BadDataError
            else:
                raise BadUnitError
#x = BMI_Index()
#a = x.Index_Calculator(1.75,80)
#print(type(a))
