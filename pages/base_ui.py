from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import settings



class BaseUI:
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
        elements = WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_all_elements_located(locator))
        for element in elements:
            texts.append(element.text)
        return texts

    def is_element_invisible(self, locator):
        try:
            WebDriverWait(self.driver, self.timeout).until(EC.invisibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def is_element_visible(self, locator):
        try:
            WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def get_element_attribute(self, locator, attribute):
        return WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located(locator)).get_attribute(attribute)

    def select_from_dropdown_by_visible_text(self, locator, text):
        dropdown = WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(locator))
        Select(dropdown).select_by_visible_text(text)
