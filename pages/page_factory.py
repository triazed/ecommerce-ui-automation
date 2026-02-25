from pages.base_page import BasePage
from pages.components.header import Header
from pages.register_page import RegisterPage


class PageFactory:
    def __init__(self, driver):
        self.driver = driver
        self.base_page = BasePage(driver)
        self.header = Header(driver)
        self.register_page = RegisterPage(driver)