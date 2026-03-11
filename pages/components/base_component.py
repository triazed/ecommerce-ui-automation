from selenium.common import TimeoutException
from config import settings
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseComponent:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = settings.DEFAULT_TIMEOUT

    def click_element(self, locator):
        WebDriverWait(self.driver, self.timeout).until(EC.element_to_be_clickable(locator)).click()

    def set_text(self, locator, text):
        element = WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(locator))
        element.send_keys(text)

    def get_text(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(locator)).text

    def is_element_visible(self, locator):
        try:
            WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def get_texts(self, locator):
        texts = []
        items = WebDriverWait(self.driver, self.timeout).until(lambda d: d.find_elements(*locator))
        for item in items:
            texts.append(item.text)
        return texts
