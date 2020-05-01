from behave import given, when, then  # pylint: disable=no-name-in-module
from BMI_Index_calculator import BMI_Index_calculator
#This will the place to import your BDD developed program


@given('I have entered the {height:d} and I have entered the {weight:d} into BMI Index calculator')
def enter_first_num(context, height, weight):
    context.height = height
    context.weight = weight
#what with second given with and


@when('I click Index Calculator')
def click_add(context):
    context.BMI_Index_calculator = BMI_Index_calculator()
    context.result = context.BMI_Index_calculator.Index_Calculator(context.height, context.weight)


@then('I should see the BMI body Index called {BMI_Index:d}')
def control_res(context, BMI_Index):
    assert context.result == BMI_Index

