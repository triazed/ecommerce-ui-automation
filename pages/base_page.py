from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import settings

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = settings.DEFAULT_TIMEOUT

    def navigate_to(self, url):
        self.driver.get(url)

    def click_element(self, locator):
        WebDriverWait(self.driver, self.timeout).until(EC.element_to_be_clickable(locator)).click()

    def set_text(self, locator, text):
        element = WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(locator))
        element.send_keys(text)

    def clear_and_set_text(self, locator, text):
        element = WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(locator)).text

    def get_texts(self, locator):
        texts = []
        elements = WebDriverWait(self.driver, self.timeout).until(lambda d: d.find_elements(*locator))
        for element in elements:
            texts.append(element.text)
        return texts

    def is_element_visible(self, locator):
        try:
            WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def get_element_attribute(self, locator, attribute):
        return WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(locator)).get_attribute(attribute)


