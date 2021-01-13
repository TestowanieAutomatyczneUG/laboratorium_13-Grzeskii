Feature: testing calculator using behave

  Scenario: Test for adding
    Given Calculator class is correct
    When x is 3 and y is 5 and operation is "+"
    Then output should be 8


  Scenario: Test for subtracting
    Given Calculator class is correct
    When x is 5 and y is 2 and operation is "-"
    Then output should be 3


  Scenario: Test for multiplication
    Given Calculator class is correct
    When x is 5 and y is 5 and operation is "*"
    Then output should be 25


  Scenario: Test for division
    Given Calculator class is correct
    When x is 8 and y is 4 and operation is "/"
    Then output should be 2


  Scenario: Test for wrong type of x
    Given Calculator class is correct
    When x is "8" and y is 1 and operation is "+"
    Then output should be "Wrong x/y type"


  Scenario: Test for wrong type of y
    Given Calculator class is correct
    When x is 5 and y is "1" and operation is "-"
    Then output should be "Wrong x/y type"


  Scenario: Test for wrong type of operation
    Given Calculator class is correct
    When x is 1 and y is 1 and operation is 5
    Then output should be "Wrong operation type"


  Scenario: Test for adding negative numbers
    Given Calculator class is correct
    When x is -5 and y is 10 and operation is "+"
    Then output should be 5