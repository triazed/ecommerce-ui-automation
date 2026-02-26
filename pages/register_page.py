from pages.base_page import BasePage
from locators.register_page_locators import RegisterPageLocators


class RegisterPage(BasePage):

    # Registration form
    def set_first_name(self, first_name):
        self.set_text(RegisterPageLocators.FIRST_NAME_INPUT, first_name)

    def set_last_name(self, last_name):
        self.set_text(RegisterPageLocators.LAST_NAME_INPUT, last_name)

    def set_email(self, email):
        self.set_text(RegisterPageLocators.EMAIL_INPUT, email)

    def set_password(self, password):
        self.set_text(RegisterPageLocators.PASSWORD_INPUT, password)

    def set_confirm_password(self, password):
        self.set_text(RegisterPageLocators.PASSWORD_CONFIRM_INPUT, password)

    def click_register_button(self):
        self.click_element(RegisterPageLocators.REGISTER_BUTTON)

    def register(self, first_name, last_name, email, password):
        self.set_first_name(first_name)
        self.set_last_name(last_name)
        self.set_email(email)
        self.set_password(password)
        self.set_confirm_password(password)
        self.click_register_button()

    # Registration result page
    def is_registration_completed(self):
        return self.is_element_visible(RegisterPageLocators.REGISTRATION_COMPLETED_MESSAGE)

