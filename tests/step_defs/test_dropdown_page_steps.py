from assertpy import assert_that
from pytest_bdd import scenarios, given, when, then, parsers
from pages.dropdown_page import DropdownPage

scenarios('../features/test_dropdown_page.feature')


@given('open the dropdown page')
def load_page(browser):
    dropdown_page = DropdownPage(browser)
    dropdown_page.load_page()


@when("the user select 'Option 1'")
def select_option1(browser):
    dropdown_page = DropdownPage(browser)
    dropdown_page.select_by_text('Option 1')


@then('the selected option is the first one')
def check_first_option_selected(browser):
    dropdown_page = DropdownPage(browser)
    assert_that(dropdown_page.is_value_selected('1')).is_true()


@when("the user select 'Option 2'")
def select_option2(browser):
    dropdown_page = DropdownPage(browser)
    dropdown_page.select_by_text('Option 2')


@then('the selected option is the second one')
def check_second_option_selected(browser):
    dropdown_page = DropdownPage(browser)
    assert_that(dropdown_page.is_value_selected('2')).is_true()


@then("the subtitle is 'Dropdown List'")
def check_subtitle(browser):
    dropdown_page = DropdownPage(browser)
    assert dropdown_page.get_subtitle() == 'Dropdown List'


@then('the user is on the current url')
def check_url(browser):
    dropdown_page = DropdownPage(browser)
    assert dropdown_page.URL == dropdown_page.get_current_url()



