Feature: calculator
As a BDD Test User, I want to see the sum and substraction of two numbers, so that I
will be able to add any two numbers

Scenario Outline: Add two numbers
    Given I have entered <number1> and <number2> into calculator
    #    And I have entered <number2> into calculator
    When I click add
    Then I should see the sum called <result>

    Examples:

    | number1| number2| result|
    |       5|       2|      7|
    |      10|      12|     22|
    |      -5|      20|     15|

Scenario Outline: substract two numbers
    Given I have entered <number1> and <number2> into calculator
    When I click substract
    Then I should see the result called <result>

    Examples:
    | number1| number2| result|
    |       5|       4|      1|
    |      10|      15|     -5|
    |      -5|      20|    -25|
    


