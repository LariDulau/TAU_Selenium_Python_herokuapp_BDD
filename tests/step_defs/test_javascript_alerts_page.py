from pytest_bdd import scenarios, given, when, then
from pages.javascript_alerts_page import AlertsPage

scenarios('../features/test_javascript_alerts_page.feature')


@given('open the alert page')
def load_page(browser):
    alerts_page = AlertsPage(browser)
    alerts_page.load_page()


@when('the user open alert')
def open_alert(browser):
    alerts_page = AlertsPage(browser)
    alerts_page.open_alert()


@when('the user open confirm')
def open_confirm(browser):
    alerts_page = AlertsPage(browser)
    alerts_page.open_confirm()


@when('the user open prompt')
def open_prompt(browser):
    alerts_page = AlertsPage(browser)
    alerts_page.open_prompt()


@when('the user click OK')
def accept_alert(browser):
    alerts_page = AlertsPage(browser)
    alerts_page.accept_alert()


@when('the user click Cancel')
def cancel_alert(browser):
    alerts_page = AlertsPage(browser)
    alerts_page.cancel_alert()


@when("the user insert 'Java Alerts'")
def insert_text(browser):
    alerts_page = AlertsPage(browser)
    alerts_page.insert_alert('Java Alerts')


@then("'You successfully clicked an alert' is displayed")
def check_message(browser):
    alerts_page = AlertsPage(browser)
    assert alerts_page.get_alert_result() == 'You successfully clicked an alert'


@then("'You clicked: Ok' is displayed")
def check_message(browser):
    alerts_page = AlertsPage(browser)
    assert alerts_page.get_alert_result() == 'You clicked: Ok'


@then("'You clicked: Cancel' is displayed")
def check_message(browser):
    alerts_page = AlertsPage(browser)
    assert alerts_page.get_alert_result() == 'You clicked: Cancel'


@then("'You entered: null' is displayed")
def check_message(browser):
    alerts_page = AlertsPage(browser)
    assert alerts_page.get_alert_result() == 'You entered: null'


@then("'You entered:' is displayed")
def check_message(browser):
    alerts_page = AlertsPage(browser)
    assert alerts_page.get_alert_result() == 'You entered:'


@then("'You entered: Java Alerts' is displayed")
def check_message(browser):
    alerts_page = AlertsPage(browser)
    assert alerts_page.get_alert_result() == 'You entered: Java Alerts'
