from behave import *
from hamcrest.core import assert_that, equal_to
from selenium.webdriver.common.by import By
from page_object import locators
from page_object.LoginPage import LoginPage


@given('Navigate to login page with URL "{url}"')
def navigate_to_login_page(context, url):
    context.driver.get(url)


@when('Input valid username "{username}"')
def input_username(context, username):
        LoginPage(context.driver).input_email(locators.LOG_IN['USERNAME'])


@step('When Input valid password "{password}"')
def input_password(context,password):
    if (password == 'Duy Nguyen'):
        LoginPage(context.driver).input_password(locators.LOG_IN['PASSWORD'])


@step("Click login button")
def click_login_button(context):
    LoginPage(context.driver).click_login_button()


@then('Login successfully and navigate to homepage with user name "{username}"')
def verify_title(context, username):
    actual_username = LoginPage(context.driver).get_text(locators.HOME['THUMNAILS_USER_DROPDOWN'])
    assert_that(actual_username, equal_to(username), 'Verify application user name ')
