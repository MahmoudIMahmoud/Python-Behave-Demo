from behave import *
@given(u'a setup for the scenario')
def step_impl(context):
    print(u'STEP: Given a setup for the scenario')


@when(u'some action with parameter {param} is done')
def step_impl(context,param):
    print(u'STEP: When some action is done')
    print(f"The parameter passed is {param}")
    


@then(u'I should found something')
def step_impl(context):
    print(u'STEP: Then I should found something')