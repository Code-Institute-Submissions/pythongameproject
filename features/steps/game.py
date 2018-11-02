from behave import *
from Riddle import Riddle


@given(u'we are answering a riddle')
def step_impl(context):
    context.riddle = Riddle()
    context.correct = None


@given(u'the riddle "{question}" is asked')
def step_impl(context, question):
    context.riddle.question = question


@given(u'the correct answer is "{answer}"')
def step_impl(context, answer):
    context.riddle.answer = answer


@when(u'we give the answer "{answer}"')
def step_impl(context, answer):
    context.correct = context.riddle.checkAnswer(answer)


@then(u'answer is {correct}')
def step_impl(context, correct):
    assert context.correct is (correct == "correct")