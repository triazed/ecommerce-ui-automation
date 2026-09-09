import pytest
from test_data.login_data import invalid_email_data, invalid_password_data, non_existent_user_data
from test_data.expectations import CUSTOMER_NOT_FOUND
import allure


@allure.parent_suite("UI Tests")
@allure.suite("Login")
class TestLogin:

    @allure.feature("Login")
    @allure.story("Registered user login")
    @allure.title("Registered user can successfully log in")
    def test_successful_login(self, pages, registered_user):
        pages.login_page.open()
        pages.login_page.login(registered_user["email"], registered_user["password"])
        with allure.step("Verify successful login"):
            assert pages.header.is_logout_button_visible()

    @allure.feature("Login")
    @allure.story("Login with invalid email")
    @allure.title("Login with invalid email fails validation")
    @pytest.mark.parametrize("email, error_message", invalid_email_data)
    def test_login_with_invalid_email(self, pages, email, error_message):
        pages.login_page.open()
        pages.login_page.set_email(email)
        pages.login_page.click_login_button()
        with allure.step("Verify login failed"):
            assert pages.login_page.get_email_error_message() == error_message

    @allure.feature("Login")
    @allure.story("Login with non-existent email")
    @allure.title("Login with non-existent email is rejected")
    def test_login_with_non_existent_email(self, pages):
        pages.login_page.open()
        pages.login_page.login(non_existent_user_data["email"], non_existent_user_data["password"])
        with allure.step("Verify login failed"):
            assert pages.login_page.get_validation_error_message() == CUSTOMER_NOT_FOUND

    @allure.feature("Login")
    @allure.story("Login with invalid password")
    @allure.title("Login with invalid password is rejected")
    @pytest.mark.parametrize("password, error_message", invalid_password_data)
    def test_login_with_invalid_password(self, pages, registered_user, password, error_message):
        pages.login_page.open()
        pages.login_page.login(registered_user["email"], password)
        with allure.step("Verify login failed"):
            assert pages.login_page.get_validation_error_message() == error_message
