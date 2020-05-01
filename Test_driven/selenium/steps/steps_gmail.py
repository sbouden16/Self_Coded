import time
from behave import given, when, then
from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

#from selenium.webdriver.support.ui import WebDriverWait
"""
def before_scenario(context, scenario):
    context.driver = webdriver.Firefox()
    context.driver = implicitly_wait(5)


def after_scenario(context, scenario):
    context.driver.quit()
"""

@given("user is on gmail portal")
def step_start_page(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&flowName=GlifWebSignIn&flowEntry=ServiceLogin")


@when('user fills the username {username} and password {password} form and submits it')
def step_set_login_in(context, username, password):
    context.driver.find_element_by_id('identifierId').send_keys(username)
    context.driver.find_element_by_id('identifierNext').click()
    time.sleep(5)
    #assert context.driver.find_element_by_id("forgotPassword")
    #context.driver.find_element_by_class_name("Xb9hP").click()
    context.driver.find_element_by_name("password").send_keys(password)
    context.driver.find_element_by_id("passwordNext").click()
    time.sleep(5)
    #context.driver.find_element_by_id('CwaK9').click()


@then("user can access his mails")
def step_correct_log_webpage(context):
    assert context.driver.find_element_by_class_name("Xb9hP")

"""

@when('user fills the invalidusername {invalidusername} and invalidpassword {invalidpassword} form and submits it')
def step_set_login_in(context, invalidusername, invalidpassword):
    context.driver.find_element_by_id('login').send_keys(invalidusername)
    context.driver.find_element_by_id('password').send_keys(invalidpassword)
    context.driver.find_element_by_id('btnSubmit').click()


@then('user will see a log in error message')
def step_set_login_in(context):
    try:
       msg = context.driver.find_element_by_class_name("Error-msg")
       assert msg.text == "Niestety podany login lub hasło jest błędne."
       context.driver.save_screenshot("bad-login.png")
    except:
       print("Test failed!!!")
    context.driver.save_screenshot("bad-login.png")
"""
