from locators.login_page_locators import LoginPageLocators
from pages.base_ui import BaseUI
from config.urls import LOGIN_URL

class LoginPage(BaseUI):

    URL = LOGIN_URL

    def open(self):
        self.navigate_to(self.URL)

    # Login form
    def set_email(self, email):
        self.set_text(LoginPageLocators.EMAIL_INPUT, email)

    def set_password(self, password):
        self.set_text(LoginPageLocators.PASSWORD_INPUT, password)

    def click_login_button(self):
        self.click_element(LoginPageLocators.LOGIN_BUTTON)

    def login(self, email, password):
        self.set_email(email)
        self.set_password(password)
        self.click_login_button()

    # Login form validation errors
    def get_validation_error_message(self):
        return self.get_text(LoginPageLocators.LOGIN_ERROR_MESSAGE)
