from behave import *
from sample.Fizzbuzz import FizzBuzz
from assertpy import *


@given(u'Fizzbuzz class is correct')
def step_impl(context):
    context.fb = FizzBuzz()


@when(u'the input is 3')
def step_impl(context):
    context.result = context.fb.game(3)


@then(u'the output should be "Fizz"')
def step_impl(context):
    assert_that(context.result).is_equal_to("Fizz")


@when(u'the input is 10')
def step_impl(context):
    context.result = context.fb.game(10)


@then(u'the output should be "Buzz"')
def step_impl(context):
    assert_that(context.result).is_equal_to("Buzz")


@when(u'the input is 30')
def step_impl(context):
    context.result = context.fb.game(30)


@then(u'the output should be "FizzBuzz"')
def step_impl(context):
    assert_that(context.result).is_equal_to("FizzBuzz")


@when(u'the input is 7')
def step_impl(context):
    context.result = context.fb.game(7)


@then(u'the output should be "Indivisible number"')
def step_impl(context):
    assert_that(context.result).is_equal_to("Indivisible number")


@when(u'the input is "8"')
def step_impl(context):
    context.result = context.fb.game("8")


@then(u'the output should be "TypeError"')
def step_impl(context):
    assert_that(context.result).is_equal_to("TypeError")
