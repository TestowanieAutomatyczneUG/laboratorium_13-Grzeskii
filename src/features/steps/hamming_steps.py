from behave import *
from sample.Hamming import Hamming
from assertpy import *

h = Hamming()


@given(u'two strands')
def step_impl(context):
    context.strands = context.text.replace('\r', '').split(',')



@when(u'they are the same')
def step_impl(context):
    context.result = h.distance(context.strands[0], context.strands[1])


@then(u'output should be 0')
def step_impl(context):
    assert_that(context.result).is_equal_to(0)


@when(u'they are different')
def step_impl(context):
    context.result = h.distance(context.strands[0], context.strands[1])


@then(u'output should be 4')
def step_impl(context):
    assert_that(context.result).is_equal_to(4)


@then(u'output should be 9')
def step_impl(context):
    assert_that(context.result).is_equal_to(9)


@when(u'they are not same length')
def step_impl(context):
    context.result = h.distance(context.strands[0], context.strands[1])


@then(u'output should be "Strands should be the same length"')
def step_impl(context):
    assert_that(context.result).is_equal_to("Strands should be the same length")


@when(u'type of first is not str')
def step_impl(context):
    context.result = h.distance(int(context.strands[0]), context.strands[1])


@when(u'type of second is not str')
def step_impl(context):
    context.result = h.distance(context.strands[0], int(context.strands[1]))


@then(u'output should be "Wrong type of strands"')
def step_impl(context):
    assert_that(context.result).is_equal_to("Wrong type of strands")