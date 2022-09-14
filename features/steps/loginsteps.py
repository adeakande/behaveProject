from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

@given('user launches the browser')
def launchBrowser(context):
    context.driver = webdriver.Chrome()



@when('user enters the Swag Labs URL')
def enterURL(context):
    context.driver.get("https://www.saucedemo.com/")


@when('user opens the Login page')
def openLoginPage(context):
    context.driver.find_element(By.XPATH,"/html/head/title").is_displayed()
    assert True

#Note that parameter values are in curly braces
@when('user enters the username "{standard_user}" and password "{secret_sauce}"')
def enterLoginDetails(context, standard_user, secret_sauce):
    context.driver.find_element(By.ID,"user-name").send_keys("standard_user")
    context.driver.find_element(By.ID, "password").send_keys("secret_sauce")

@when('user clicks on the login button')
def clickLoginButton(context):
    context.driver.find_element(By.ID, "login-button").click()

#To capture the text value from the homepage
@then('user will be logged in to Swag Labs')
def homePage(context):
    try:
        text = context.driver.find_element(By.XPATH, "//*[@id='item_4_title_link']/div").text
    except:
        context.driver.close()
        assert False,"Test Failed"
    if text == "Sauce Labs Backpack":
        context.driver.close()
        assert True,"Test Passed"




