from behave import *
from sample.Calculator import Calculator
from assertpy import *


@given(u'Calculator class is correct')
def step_impl(context):
    context.calc = Calculator()


@when(u'x is 3 and y is 5 and operation is "+"')
def step_impl(context):
    context.result = context.calc.game(3, "+", 5)


@then(u'output should be 8')
def step_impl(context):
    assert_that(context.result).is_equal_to(8)


@when(u'x is 5 and y is 2 and operation is "-"')
def step_implt(context):
    context.result = context.calc.game(5, "-", 2)


@then(u'output should be 3')
def step_impl(context):
    assert_that(context.result).is_equal_to(3)


@when(u'x is 5 and y is 5 and operation is "*"')
def step_impl(context):
    context.result = context.calc.game(5, "*", 5)


@then(u'output should be 25')
def step_impl(context):
    assert_that(context.result).is_equal_to(25)


@when(u'x is 8 and y is 4 and operation is "/"')
def step_impl(context):
    context.result = context.calc.game(8, "/", 4)


@then(u'output should be 2')
def step_impl(context):
    assert_that(context.result).is_equal_to(2)


@when(u'x is "8" and y is 1 and operation is "+"')
def step_impl(context):
    context.result = context.calc.game("8", "+", 1)


@when(u'x is 5 and y is "1" and operation is "-"')
def step_impl(context):
    context.result = context.calc.game(5, "-", "1")


@then(u'output should be "Wrong x/y type"')
def step_impl(context):
    assert_that(context.result).starts_with("Wrong").ends_with("type")


@when(u'x is 1 and y is 1 and operation is 5')
def step_impl(context):
    context.result = context.calc.game(1, 5, 1)


@then(u'output should be "Wrong operation type"')
def step_impl(context):
    assert_that(context.result).contains("operation").ends_with("type")


@when(u'x is -5 and y is 10 and operation is "+"')
def step_impl(context):
    context.result = context.calc.game(-5, "+", 10)


@then(u'output should be 5')
def step_impl(context):
    assert_that(context.result).is_equal_to(5)
