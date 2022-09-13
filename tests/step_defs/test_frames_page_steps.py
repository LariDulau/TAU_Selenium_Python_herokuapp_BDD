from pytest_bdd import scenarios, given, when, then
from pages.frames_page import FramesPage

scenarios('../features/test_frames_page.feature')


@given('open the frames page')
def open_page(browser):
    frames_page = FramesPage(browser)
    frames_page.load_page()


@when('the user click on nested frames link')
def click_on_nested_frames(browser):
    frames_page = FramesPage(browser)
    frames_page.click_nested_frames()


@then('the user is on the current url')
def current_url(browser):
    frames_page = FramesPage(browser)
    assert frames_page.URL == frames_page.get_current_url()


@then('the user is not on the current url')
def current_url(browser):
    frames_page = FramesPage(browser)
    assert frames_page.URL != frames_page.get_current_url()


@then('the subtitle is displayed')
def check_subtitle(browser):
    frames_page = FramesPage(browser)
    assert frames_page.get_subtitle() == 'Frames'




