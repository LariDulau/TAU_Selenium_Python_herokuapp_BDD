from pytest_bdd import scenarios, given, when, then
from pages.iframe_page import IFramePage


scenarios('../features/test_iframe_page.feature')


@given('open the iframe page')
def open_page(browser):
    iframe_page = IFramePage(browser)
    iframe_page.load_page()


# @when('the user write "The car is new"')
# def insert_text(browser):
#     iframe_page = IFramePage(browser)
#     iframe_page.write('The car is new')
#
#
# @then('"The car is new" is displayed')
# def check_text(browser):
#     iframe_page = IFramePage(browser)
#     assert iframe_page.get_text() == 'The car is new'


@then('the user is on the iframe page')
def check_url(browser):
    iframe_page = IFramePage(browser)
    assert iframe_page.get_url() == iframe_page.URL



@then('the subtitle is displayed')
def check_subtitle(browser):
    iframe_page = IFramePage(browser)
    assert iframe_page.get_title_page() == 'An iFrame containing the TinyMCE WYSIWYG Editor'

