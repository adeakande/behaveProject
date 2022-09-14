from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given('launch the browser')
def launchBrowser(context):
    #context.driver = webdriver.Chrome(executable_path="C:\SeleniumDrivers\chromedriver.exe")
    context.driver = webdriver.Edge()       #You can specify which browser you want to run

@when('enter the Swag Labs URL')
def enterURL(context):
    context.driver.get("https://www.saucedemo.com/")

@then('verify that the title is present on the login page')
def verifyTitle(context):
    context.driver.find_element(By.XPATH,"/html/head/title").is_displayed()
    assert True

@then('close the browser')
def closeBrowser(context):
    context.driver.close()





# @given('launch the browser')
# def launchBrowser(context):
#     #context.driver = webdriver.Chrome(executable_path="C:\SeleniumDrivers\chromedriver.exe")
#     context.driver = webdriver.Edge()       #You can specify which browser you want to run
#
# @when('enter the Swag Labs URL')
# def enterURL(context):
#     context.driver.get("https://www.saucedemo.com/")
#
# @then('verify that the logo is displayed on the login page')
# def verifyLogo(context):
#     context.driver.find_element(By.XPATH,"//*[@id='root']/div/div[1]").is_displayed()
#     assert True
#
# @then('close the browser')
# def closeBrowser(context):
#     context.driver.close()
