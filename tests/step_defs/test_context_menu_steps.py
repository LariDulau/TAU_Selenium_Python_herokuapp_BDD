from pytest_bdd import scenarios, given, when, then
from pages.context_menu_page import ContextMenuPage

scenarios('../features/test_context_menu_page.feature')


@given('open the context menu page')
def open_page(browser):
    context_menu_page = ContextMenuPage(browser)
    context_menu_page.load_page()


@when('the user click on the menu')
def open_menu(browser):
    context_menu_page = ContextMenuPage(browser)
    context_menu_page.open_menu()


@when('the user click accept alert')
def accept_alert(browser):
    context_menu_page = ContextMenuPage(browser)
    context_menu_page.accept_alert()


@then('the user is on the context menu page')
def check_url(browser):
    context_menu_page = ContextMenuPage(browser)
    assert context_menu_page.URL == context_menu_page.get_current_url()


@then("'You selected a context menu' message is displayed")
def check_message(browser):
    context_menu_page = ContextMenuPage(browser)
    assert context_menu_page.get_text_alert() == 'You selected a context menu'





