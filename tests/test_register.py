import pytest
from test_data.registration_data import invalid_email_data, invalid_password_data
from test_data.registration_data import new_user
from test_data.expectations import (REGISTRATION_RESULT_SUCCESS_MESSAGE, EMAIL_EXISTS_ERROR_MESSAGE, EMPTY_REG_PASSWORD, INCORRECT_CONFIRM_PASSWORD, MISSING_REG_FIRST_NAME, MISSING_REG_LAST_NAME)


class TestRegister:

    def test_successful_registration(self, pages):
        pages.register_page.open()
        user = new_user()
        pages.register_page.register(user)
        assert pages.register_page.get_registration_result_message() == REGISTRATION_RESULT_SUCCESS_MESSAGE
        assert pages.header.is_logout_button_visible()

    def test_registration_with_existing_email(self, pages, registered_user):
        pages.register_page.open()
        pages.register_page.register(registered_user)
        assert pages.register_page.get_validation_error_message() == EMAIL_EXISTS_ERROR_MESSAGE

    @pytest.mark.parametrize("email, error_message", invalid_email_data)
    def test_registration_with_invalid_email(self, pages, email, error_message):
        pages.register_page.open()
        registration_data = new_user()
        registration_data["email"] = email
        pages.register_page.register(registration_data)
        assert pages.register_page.get_email_validation_error_message() == error_message

    @pytest.mark.parametrize("password, error_message", invalid_password_data)
    def test_registration_with_invalid_password(self, pages, password, error_message):
        pages.register_page.open()
        registration_data = new_user()
        registration_data["password"] = password
        pages.register_page.register(registration_data)
        assert pages.register_page.get_password_validation_error_message() == error_message

    def test_registration_with_missing_password(self, pages):
        pages.register_page.open()
        registration_data = new_user()
        registration_data["password"] = ""
        pages.register_page.register(registration_data)
        assert pages.register_page.get_confirm_password_validation_error_message() == EMPTY_REG_PASSWORD

    def test_registration_with_invalid_confirm_password(self, pages):
        pages.register_page.open()
        registration_data = new_user()
        registration_data["confirm_password"] = "123456"
        pages.register_page.register(registration_data)
        assert pages.register_page.get_confirm_password_validation_error_message() == INCORRECT_CONFIRM_PASSWORD

    def test_registration_with_missing_first_name(self, pages):
        pages.register_page.open()
        registration_data = new_user()
        registration_data["first_name"] = ""
        pages.register_page.register(registration_data)
        assert pages.register_page.get_first_name_validation_error_message() == MISSING_REG_FIRST_NAME

    def test_registration_with_missing_last_name(self, pages):
        pages.register_page.open()
        registration_data = new_user()
        registration_data["last_name"] = ""
        pages.register_page.register(registration_data)
        assert pages.register_page.get_last_name_validation_error_message() == MISSING_REG_LAST_NAME
