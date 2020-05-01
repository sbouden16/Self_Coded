from behave import given, when, then  # pylint: disable=no-name-in-module
from calc import calculator
#This will the place to import your BDD developed program


@given('I have entered {number1:d} and {number2:d} into calculator')
def enter_first_num(context, number1, number2):
    context.number1=number1
    context.number2 = number2
#what with second given with and

@when('I click add')
def click_add(context):
    context.calculator=calculator()
    context.result = context.calculator.add(context.number1, context.number2)


@then('I should see the sum called {result:d}')
def control_res(context, result):
    assert context.result==result


#Substraction BDD 

@when('I click substract')
def click_substract(context):
    context.calculator = calculator()
    context.result = context.calculator.substract(context.number1, context.number2)

@then('I should see the result called {result:d}')
def control_res_2(context, result):
    assert context.result == result
