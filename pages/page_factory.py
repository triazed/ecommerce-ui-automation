from pages.base_page import BasePage
from pages.components.header import Header
from pages.register_page import RegisterPage


class PageFactory:
    def __init__(self, driver):
        self.driver = driver

    @property
    def base_page(self):
        return BasePage(self.driver)

    @property
    def header(self):
        return Header(self.driver)

    @property
    def register_page(self):
        return RegisterPage(self.driver)
