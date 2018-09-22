from behave import *
from Riddle import Riddle


@given(u'we are answering a riddle')
def step_impl(context):
    context.riddle = Riddle()
    context.correct = None

@given(u'the riddle "what is the colour" is asked')
def step_impl(context):
    context.riddle.question = "what is the colour"

@given(u'the correct answer is "yellow"')
def step_impl(context):
    context.riddle.answer = "yellow"

@when(u'we give the answer "yellow"')
def step_impl(context):
    context.correct = context.riddle.checkAnswer("yellow")

@then(u'answer is correct')
def step_impl(context):
    assert context.correct is True

@when(u'we give the answer "red"')
def step_impl(context):
    context.correct = context.riddle.checkAnswer("red")


@then(u'answer is incorrect')
def step_impl(context):
    assert context.correct is False
