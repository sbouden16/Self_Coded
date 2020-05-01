'''
print('\t\t\t BMI Calculator')
print('\t\t\t By Abdinasir Hussein')
print('\n Hello, this is a BMI Calculator!')

class BadUnitError(Exception):
    pass
class BadDataError(Exception):
    pass

unit = input('Do you wish to enter metric (M) units, imperial (I) units or Quit (Q):  ').upper()
while unit != "Q":

    if unit == "M":
        height = float(input('Please enter your height input meters(decimals): '))
        weight = int(input('Please enter your weight input kg: '))
        bmi = weight/(height*height)

while bmi > 1:
                if bmi <= 18.5:
                print('Your BMI is', bmi, 'which means you are underweight.')
                unit = input(
                    'Do you wish to enter metric (M) units, imperial (I) units or Quit (Q):  ').upper()
                height = float(
                    input('Please enter your height input meters(decimals): '))
                weight = float(input('Please enter your weight input kg: '))
                bmi = weight/(height*height)

            elif bmi > 18.5 and bmi < 25:
                print('Your BMI is', bmi, 'which means you are normal.')
                unit = input(
                    'Do you wish to enter metric (M) units, imperial (I) units or Quit (Q):  ').upper()
                height = float(
                    input('Please enter your height input meters(decimals): '))
                weight = float(input('Please enter your weight input kg: '))
                bmi = weight/(height*height)
            elif bmi > 25 and bmi < 30:
                print('your BMI is', bmi, 'overweight.')
                unit = input(
                    'Do you wish to enter metric (M) units, imperial (I) units or Quit (Q):  ').upper()
                height = float(
                    input('Please enter your height input meters(decimals): '))
                weight = float(input('Please enter your weight input kg: '))
                bmi = weight/(height*height)
            elif bmi > 30:
                print('Your BMI is', bmi, 'which means you are obese.')
                unit = input(
                    'Do you wish to enter metric (M) units, imperial (I) units or Quit (Q):  ').upper()
                height = float(
                    input('Please enter your height input meters(decimals): '))
                weight = float(input('Please enter your weight input kg: '))
                bmi = weight/(height*height)
        
        else:
            try:
                print("You have entered wrong data")
                raise BadDataError
            except BadDataError:
                height = float(input('Please enter your height input meters(decimals): '))
                weight = float(input('Please enter your weight input kg: '))
                bmi = weight/(height*height)
    else:
        raise BadUnitError

'''


class BadUnitError(Exception):
    pass


class BadDataError(Exception):
    pass
class BMI_Index_calculator():
        def Index_Calculator(self,height,weight):
            bmi = weight/(height*height)
            if bmi > 1:
                if bmi <= 18.5:
                    print('Your BMI is', bmi, 'which means you are underweight.')
                    return bmi
                

                elif bmi > 18.5 and bmi < 25:
                    print('Your BMI is', bmi, 'which means you are normal.')
                    return bmi
               
                elif bmi > 25 and bmi < 30:
                    print('your BMI is', bmi, 'overweight.')
                    return bmi
                
                elif bmi > 30:
                    print('Your BMI is', bmi, 'which means you are obese.')
                    return bmi
            else:
                if bmi > 0 and bmi <= 1:
                    raise BadDataError
                else:
                    raise BadUnitError
        
#x = BMI_Index_calculator()
#print(x.Index_Calculator(1.75,80))              

"""
    elif unit == 'I':
        height = int(input('Please enter your height input inputches(whole number): '))
        weight = int(input('Please enter your weight input pounds(whole number): '))
        bmi = (weight*703)/(height*height)

        if bmi <= 18.5:
            print('Your BMI is', bmi, 'which means you are underweight.')

        elif bmi > 18.5 and bmi < 25:
            print('Your BMI is', bmi, 'which means you are normal.')

        elif bmi > 25 and bmi < 30:
            print('Your BMI is', bmi, 'which means you are overweight')

        elif bmi > 30:
            print('Your BMI is', bmi, 'which means you are obese.')

        else:
            print('There is an error with your input')
            print('Please check you have entered whole numbers\n'
              'and decimals were asked.')
            raise BadDataError
        unit = input(
            'Do you wish to enter metric (M) units, imperial (I) units or Quit (Q):  ').upper()
    else:
        raise BadUnitError


"""

'''

heights = [1.4, 1.74, 1.76, 1.85, 1.92, 1.45]
weights = [85, 76, 101, 67, 100, 96]

for i in heights:
    for j in weights:
        x = i*j
        print("multiply {} for {} and get = {}""".format(i,j,x))

'''
