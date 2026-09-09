from config.urls import REGISTER_URL
from pages.base_ui import BaseUI
from locators.register_page_locators import RegisterPageLocators
import allure


class RegisterPage(BaseUI):
    URL = REGISTER_URL

    @allure.step("Open registration page")
    def open(self):
        self.navigate_to(self.URL)

    # Registration form
    def set_first_name(self, registration_data):
        self.set_text(RegisterPageLocators.FIRST_NAME_INPUT, registration_data["first_name"])

    def set_last_name(self, registration_data):
        self.set_text(RegisterPageLocators.LAST_NAME_INPUT, registration_data["last_name"])

    def set_email(self, registration_data):
        self.set_text(RegisterPageLocators.EMAIL_INPUT, registration_data["email"])

    def set_password(self, registration_data):
        self.set_text(RegisterPageLocators.PASSWORD_INPUT, registration_data["password"])

    def set_confirm_password(self, registration_data):
        self.set_text(RegisterPageLocators.PASSWORD_CONFIRM_INPUT, registration_data["confirm_password"])

    def click_register_button(self):
        self.click_element(RegisterPageLocators.REGISTER_BUTTON)

    @allure.step("Register")
    def register(self, registration_data):
        self.set_first_name(registration_data)
        self.set_last_name(registration_data)
        self.set_email(registration_data)
        self.set_password(registration_data)
        self.set_confirm_password(registration_data)
        self.click_register_button()

    # Registration form validation errors
    def get_validation_error_message(self):
        return self.get_text(RegisterPageLocators.FORM_VALIDATION_ERROR_MESSAGE)

    def get_first_name_validation_error_message(self):
        return self.get_text(RegisterPageLocators.FIRST_NAME_VALIDATION_ERROR_MESSAGE)

    def get_last_name_validation_error_message(self):
        return self.get_text(RegisterPageLocators.LAST_NAME_VALIDATION_ERROR_MESSAGE)

    def get_email_validation_error_message(self):
        return self.get_text(RegisterPageLocators.EMAIL_VALIDATION_ERROR_MESSAGE)

    def get_password_validation_error_message(self):
        return self.get_text(RegisterPageLocators.PASSWORD_VALIDATION_ERROR_MESSAGE)

    def get_confirm_password_validation_error_message(self):
        return self.get_text(RegisterPageLocators.CONFIRM_PASSWORD_VALIDATION_ERROR_MESSAGE)

    # Registration result page
    def get_registration_result_message(self):
        return self.get_text(RegisterPageLocators.REGISTRATION_COMPLETED_MESSAGE)
