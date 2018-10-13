from behave import *
from User import User
from flask import session

@given(u'that I am authenticating a user')
def step_impl(context):
    context.user = User()
    context.user.handle = None

@when(u'I am not logged in')
def step_impl(context):
    context.user.handle = found
    context.user.password = None
    context.correct = None



@given(u'I do not currently have an account')
def step_impl(context):
    context.user.handle = None
    context.user.password = None
    context.correct = None

@when(u'I click the "Login" button')
def step_impl(context):
    context.login.page = found
    context.user.password = None
    context.correct = None

@when(u'I enter a username "micaela"')
def step_impl(context):
    context.user.handle = "micaela"
    context.correct = found

@when(u'I enter a password "password"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I enter a password "password"')


@then(u'I am taken to the "Home" page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I am taken to the "Home" page')


@then(u'I see the name "micaela" at the top of the page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I see the name "micaela" at the top of the page')


@when(u'I click the "Play Game" button')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I click the "Play Game" button')


@then(u'I am taken to the "Login" page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I am taken to the "Login" page')
