from locators.components.header_locators import HeaderLocators
from pages.base_page import BasePage


class Header(BasePage):

    def click_register_button(self):
        self.click_element(HeaderLocators.REGISTER_BUTTON)

    def click_login_button(self):
        self.click_element(HeaderLocators.LOGIN_BUTTON)

    def click_logout_button(self):
        self.click_element(HeaderLocators.LOGOUT_BUTTON)

    def is_logout_button_visible(self):
        return self.is_element_visible(HeaderLocators.LOGOUT_BUTTON)


