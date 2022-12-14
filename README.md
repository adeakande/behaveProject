# behaveProject

* Components of the BDD Structure*
Feature file -------  uses .feature 

Scenario -----------  there could be several scenarios under the feature

Steps e.g    Given
             When
             And
             Then

each scenarios contain steps


Python Behave with Selenium
--------------------------------

1. Create project
2. First Selenium Test

IDE packages to install
------------------------
install selenium package
install behave package
install gherkin cucumber bdd plugin

Selenium - Driver for browsers
-----------------------------------
chromedriver.exe
geckodriver.exe
msedgedriver.exe




@given(u'Launch the browser')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given Launch the browser')


@when(u'enter the Swag Labs URL')
def step_impl(context):
    raise NotImplementedError(u'STEP: When enter the Swag Labs URL')


@then(u'verify that the title is present on the login page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then verify that the title is present on the login page')


@then(u'close the browser')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then close the browser')


Background
--------------
For steps that are common to all the scenarios. This reduces repetition e.g.


Background: common steps
    Given user launches the browser
    When user enters the Swag Labs URL
    And user opens the Login page
    And user enters the username "standard_user" and password "secret_sauce"
    And user clicks on the login button

  Scenario: Login to Swag Labs
    Then user will be logged in to Swag Labs

  Scenario: Search product
    Then user will be logged in to Swag Labs
    Then products should be displayed on the page

  Scenario: Search for app logo
    Then user will be logged in to Swag Labs
    Then app logo should be displayed on the page


note: the Backgroung above launches the common steps first before every scenario.


Allure Behave
----------------

 pip install allure-behave                                           #install in cmd
 install allure-behave                                               #dependency in PyCharm

To execute test and to generate json report: 
------------------------------------- 

* behave features\scenariobg.feature
* behave features\swaglabslogin.feature 
* behave features\swaglabs.feature

  #Test results with json report output

* behave -f allure_behave.formatter:AllureFormatter -o reports/ features

  #Run test with allure report output  

* behave -m allure serve \report


to generate HTML reports add this to your run command
-----------------------------------------------------
allure serve reports/


















