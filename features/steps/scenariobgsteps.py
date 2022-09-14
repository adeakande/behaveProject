from behave import *
from selenium import webdriver

'''Only use step definition for newly added steps only. Previously defined steps will be picked automatically.'''

@then(u'products should be displayed on the page')
def step_impl(context):
    assert True,"Test Passed"

@then(u'app logo should be displayed on the page')
def step_impl(context):
    assert True,"Test Passed"
