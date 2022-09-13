from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class SecurePage:
    WELCOME_TEXT = (By.CSS_SELECTOR, 'h4')
    LOGOUT_BUTTON = (By.CSS_SELECTOR, '[class="button secondary radius"]')
    FLASH_TEXT = (By. ID, 'flash')


    URL = "https://the-internet.herokuapp.com/secure"


    def __init__(self, browser):
        self.browser = browser

    def load_page(self):
        self.browser.get(self.URL)

    def get_current_url(self):
        return self.browser.current_url

    def get_welcome_message(self):
        return self.browser.find_element(*self.WELCOME_TEXT).text

    def click_logout(self):
        self.browser.find_element(*self.LOGOUT_BUTTON).click()

    def is_flash_text_displayed(self):
        return self.browser.find_element(*self.FLASH_TEXT).is_displayed()

    def get_flash_message(self):
        return self.browser.find_element(*self.FLASH_TEXT).text

    def wait_for_logout_button(self):
        wait = WebDriverWait(self.browser, 5)
        wait.until(EC.element_to_be_clickable(self.LOGOUT_BUTTON))

