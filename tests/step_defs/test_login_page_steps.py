from pytest_bdd import scenarios, given, when, then, parsers
from pages.login_page import LoginPage
from pages.secure_page import SecurePage

#Scenario
scenarios('../features/test_login_page.feature')


# Shared Given Steps
@given('open the login page')
def open_page(browser):
    login_page = LoginPage(browser)
    login_page.load_page()


@when("the user type username 'tomsmith'")
def insert_username(browser):
    login_page = LoginPage(browser)
    login_page.insert_username('tomsmith')


@when("the user type password 'SuperSecretPassword!'")
def insert_password(browser):
    login_page = LoginPage(browser)
    login_page.insert_password('SuperSecretPassword!')


@when('the user click login button')
def click_login_button(browser):
    login_page = LoginPage(browser)
    login_page.click_login()


@when(parsers.cfparse('the user type username "{username}"'))
def input_username(browser, username):
    login_page = LoginPage(browser)
    login_page.insert_username(username)


@when(parsers.cfparse('the user type password "{password}"'))
def input_password(browser, password):
    login_page = LoginPage(browser)
    login_page.insert_password(password)


@then('the welcome message appears on page')
def check_welcome_message(browser):
    secure_page = SecurePage(browser)
    assert secure_page.get_welcome_message() == 'Welcome to the Secure Area. When you are done click logout below.'


@then(parsers.cfparse('"{error}" error message is displayed'))
def check_error_message(browser, error):
    login_page = LoginPage(browser)
    assert error in login_page.get_flash_message(), "Flash message is not ok"


@then("the user is on the login page")
def check_url(browser):
    login_page = LoginPage(browser)
    assert login_page.URL == login_page.get_current_url()


@then('the user is on the secure page')
def check_current_url(browser):
    secure_page = SecurePage(browser)
    assert secure_page.get_current_url() == secure_page.URL


@then(parsers.cfparse('"{message}" success message is displayed'))
def check_flash_message(browser, message):
    secure_page = SecurePage(browser)
    assert message in secure_page.get_flash_message(), "Flash message is not ok"

