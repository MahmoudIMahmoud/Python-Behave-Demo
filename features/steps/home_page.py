from behave import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

@given(u'I open the web browser')
def step_impl(context):
    print(u'STEP: Given I open the web browser')
    driver = webdriver.Chrome(ChromeDriverManager().install())
    context.driver = driver
    context.driver.maximize_window()
    context.driver.implicitly_wait(30)
    

@when(u'I navigate to home page')
def step_impl(context):
    print(u'STEP: When I navigate to home page')
    context.driver.get("https://opensource-demo.orangehrmlive.com/")


@then(u'I found a login form')
def step_impl(context):
    print(u'STEP: Then I found a login form')
    context.driver.find_elements(by='xpath', value="//button[contains(.,'Login')] ")
    context.driver.find_elements(by='xpath', value="//h5[contains(.,'Login')] ")
    time.sleep(3) # give a chance for visual validation