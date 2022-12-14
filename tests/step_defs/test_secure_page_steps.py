from pytest_bdd import scenarios, when, then, given, parsers
from pages.login_page import LoginPage
from pages.secure_page import SecurePage

# Scenario
scenarios('../features/test_secure_page.feature')


@given('open the login page')
def open_page(browser):
    login_page = LoginPage(browser)
    login_page.load_page()


@when('the user is logging in')
def login(browser):
    login_page = LoginPage(browser)
    login_page.login("tomsmith", "SuperSecretPassword!")


@when("the user click on logout button")
def click_logout_button(browser):
    secure_page = SecurePage(browser)
    secure_page.click_logout()


@then(parsers.cfparse('"{message}" success message is displayed'))
def check_flash_message(browser, message):
    secure_page = SecurePage(browser)
    assert message in secure_page.get_flash_message(), "Flash message is not ok"







