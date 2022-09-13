from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By


class ContextMenuPage:
    BOX = (By.CSS_SELECTOR, '[oncontextmenu="displayMessage()"]')


    URL = "https://the-internet.herokuapp.com/context_menu"

    def __init__(self, browser):
       self.browser = browser

    def load_page(self):
        self.browser.get(self.URL)

    def get_current_url(self):
        return self.browser.current_url

    def open_menu(self):
        actions = ActionChains(self.browser)
        actions.context_click(self.browser.find_element(*self.BOX)).perform()

    def accept_alert(self):
        alert = self.browser.switch_to.alert
        alert.accept()

    def get_text_alert(self):
        alert = self.browser.switch_to.alert
        return alert.text


