Feature: Testing Fizzbuzz using behave

    Scenario: Test for Fizz
        Given Fizzbuzz class is correct
        When the input is 3
        Then the output should be "Fizz"

    Scenario: Test for Buzz
        Given Fizzbuzz class is correct
        When the input is 10
        Then the output should be "Buzz"

    Scenario: Test for FizzBuzz
        Given Fizzbuzz class is correct
        When the input is 30
        Then the output should be "Fizzbuzz"

    Scenario: Test for Indivisible number
        Given Fizzbuzz class is correct
        When the input is 7
        Then the output should be "Indivisible number"

    Scenario: Test for wrong type
        Given Fizzbuzz class is correct
        When the input is "8"
        Then the output should be "TypeError"