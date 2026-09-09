import pytest
from test_data.registration_data import invalid_email_data, invalid_password_data
from test_data.registration_data import new_user
from test_data.expectations import (REGISTRATION_RESULT_SUCCESS_MESSAGE, EMAIL_EXISTS_ERROR_MESSAGE, EMPTY_REG_PASSWORD, INCORRECT_CONFIRM_PASSWORD, MISSING_REG_FIRST_NAME, MISSING_REG_LAST_NAME)
import allure


@allure.parent_suite("UI Tests")
@allure.suite("Registration")
class TestRegister:

    @allure.feature("Registration")
    @allure.story("Registration with valid credentials")
    @allure.title("Guest can successfully register with valid credentials")
    def test_successful_registration(self, pages):
        pages.register_page.open()
        user = new_user()
        pages.register_page.register(user)
        with allure.step("Verify registration successful"):
            assert pages.register_page.get_registration_result_message() == REGISTRATION_RESULT_SUCCESS_MESSAGE
            assert pages.header.is_logout_button_visible()

    @allure.feature("Registration")
    @allure.story("Registration with existing email")
    @allure.title("Registration with existing email is rejected")
    def test_registration_with_existing_email(self, pages, registered_user):
        pages.register_page.open()
        pages.register_page.register(registered_user)
        with allure.step("Verify registration failed"):
            assert pages.register_page.get_validation_error_message() == EMAIL_EXISTS_ERROR_MESSAGE

    @allure.feature("Registration")
    @allure.story("Registration with invalid email")
    @allure.title("Registration with invalid email fails validation")
    @pytest.mark.parametrize("email, error_message", invalid_email_data)
    def test_registration_with_invalid_email(self, pages, email, error_message):
        pages.register_page.open()
        registration_data = new_user()
        registration_data["email"] = email
        pages.register_page.register(registration_data)
        with allure.step("Verify registration failed"):
            assert pages.register_page.get_email_validation_error_message() == error_message

    @allure.feature("Registration")
    @allure.story("Registration with invalid password")
    @allure.title("Registration with invalid password fails validation")
    @pytest.mark.parametrize("password, error_message", invalid_password_data)
    def test_registration_with_invalid_password(self, pages, password, error_message):
        pages.register_page.open()
        registration_data = new_user()
        registration_data["password"] = password
        pages.register_page.register(registration_data)
        with allure.step("Verify registration failed"):
            assert pages.register_page.get_password_validation_error_message() == error_message

    @allure.feature("Registration")
    @allure.story("Registration with missing password")
    @allure.title("Registration with missing password fails validation")
    def test_registration_with_missing_password(self, pages):
        pages.register_page.open()
        registration_data = new_user()
        registration_data["password"] = ""
        pages.register_page.register(registration_data)
        with allure.step("Verify registration failed"):
            assert pages.register_page.get_confirm_password_validation_error_message() == EMPTY_REG_PASSWORD

    @allure.feature("Registration")
    @allure.story("Registration with mismatched password confirmation")
    @allure.title("Registration with mismatched password confirmation fails validation")
    def test_registration_with_invalid_confirm_password(self, pages):
        pages.register_page.open()
        registration_data = new_user()
        registration_data["confirm_password"] = "123456"
        pages.register_page.register(registration_data)
        with allure.step("Verify registration failed"):
            assert pages.register_page.get_confirm_password_validation_error_message() == INCORRECT_CONFIRM_PASSWORD

    @allure.feature("Registration")
    @allure.story("Registration with missing first name")
    @allure.title("Registration with missing first name fails validation")
    def test_registration_with_missing_first_name(self, pages):
        pages.register_page.open()
        registration_data = new_user()
        registration_data["first_name"] = ""
        pages.register_page.register(registration_data)
        with allure.step("Verify registration failed"):
            assert pages.register_page.get_first_name_validation_error_message() == MISSING_REG_FIRST_NAME

    @allure.feature("Registration")
    @allure.story("Registration with missing last name")
    @allure.title("Registration with missing last name fails validation")
    def test_registration_with_missing_last_name(self, pages):
        pages.register_page.open()
        registration_data = new_user()
        registration_data["last_name"] = ""
        pages.register_page.register(registration_data)
        with allure.step("Verify registration failed"):
            assert pages.register_page.get_last_name_validation_error_message() == MISSING_REG_LAST_NAME
