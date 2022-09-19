from pytest_bdd import scenarios, given, when, then, parsers
from pages.add_remove_elements_page import AddRemoveElementsPage

scenarios('../features/test_add_remove_page.feature')


@given('open the page')
def load_page(browser):
    add_remove_page = AddRemoveElementsPage(browser)
    add_remove_page.load_page()


@when('the user click add button')
def click_add_buton(browser):
    add_remove_page = AddRemoveElementsPage(browser)
    add_remove_page.click_add_button()


@when('the user click delete button')
def click_delete_buton(browser):
    add_remove_page = AddRemoveElementsPage(browser)
    add_remove_page.click_delete_button()


@when('the user click on the link')
def click_link(browser):
    add_remove_page = AddRemoveElementsPage(browser)
    add_remove_page.click_link()


@then('add button is displayed')
def check_add_button(browser):
    add_remove_page = AddRemoveElementsPage(browser)
    add_remove_page.is_add_button_displayed()


@then('the link is displayed')
def check_link_displyed(browser):
    add_remove_page = AddRemoveElementsPage(browser)
    add_remove_page.is_link_displayed()


@then('the user is on the elemental selenium link')
def check_elemental_link(browser):
    add_remove_page = AddRemoveElementsPage(browser)
    browser.switch_to.window(browser.window_handles[1])
    assert add_remove_page.get_current_url() == 'http://elementalselenium.com/'


@then('the title is displayed')
def check_title(browser):
    add_remove_page = AddRemoveElementsPage(browser)
    assert add_remove_page.get_title_page() == 'Add/Remove Elements'


@then('the user is on the add remove elements page')
def check_url(browser):
    add_remove_page = AddRemoveElementsPage(browser)
    assert add_remove_page.get_current_url() == 'https://the-internet.herokuapp.com/add_remove_elements/'


@then('is one delete button on the page')
def check_delete_button(browser):
    add_remove_page = AddRemoveElementsPage(browser)
    assert add_remove_page.get_number_of_delete_button() == 1


@then('no more delete button on the page')
def check_delete_button_zero(browser):
    add_remove_page = AddRemoveElementsPage(browser)
    assert add_remove_page.get_number_of_delete_button() == 0


@then('check add functionality')
def check_add_functionality(browser):
    add_remove_page = AddRemoveElementsPage(browser)
    for i in range(10):
        add_remove_page.click_add_button()
        assert add_remove_page.get_number_of_delete_button() == (i+1)


@then('check delete functionality')
def check_delete_functionality(browser):
    add_remove_page = AddRemoveElementsPage(browser)
    for i in range(10):
        add_remove_page.click_first_delete_button()
        assert add_remove_page.get_number_of_delete_button() == (10-i-1)
