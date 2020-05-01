from behave import given, when, then  # pylint: disable=no-name-in-module
from BMI_Calculator import BMI_Index

@given("I have entered the {height} and I have entered the {weight} into BMI Index calculator")
def enter_weight_height(context,height,weight):
    context.height = float(height)
    context.weight = float(weight)

@when("I make click in Index Calculator")
def click_BMI_Index(context):
    context.BMI_Calculation = BMI_Index()
    context.result = context.BMI_Calculation.Index_Calculator(context.height,context.weight)

@then("I should see the BMI body index: {Index}")
def control_response_BMI(context,Index):
    assert context.result == float(Index)
#https://behave.readthedocs.io/en/latest/parse_builtin_types.html
