import pytest
from test_data.login_data import invalid_email_data, invalid_password_data, non_existent_user_data
from test_data.expectations import CUSTOMER_NOT_FOUND


class TestLogin:

    def test_successful_login(self, pages, registered_user):
        pages.login_page.open()
        pages.login_page.login(registered_user["email"], registered_user["password"])
        assert pages.header.is_logout_button_visible()

    @pytest.mark.parametrize("email, error_message", invalid_email_data)
    def test_login_with_invalid_email(self, pages, email, error_message):
        pages.login_page.open()
        pages.login_page.set_email(email)
        pages.login_page.click_login_button()
        assert pages.login_page.get_email_error_message() == error_message

    def test_login_with_non_existent_email(self, pages):
        pages.login_page.open()
        pages.login_page.login(non_existent_user_data["email"], non_existent_user_data["password"])
        assert pages.login_page.get_validation_error_message() == CUSTOMER_NOT_FOUND

    @pytest.mark.parametrize("password, error_message", invalid_password_data)
    def test_login_with_invalid_password(self, pages, registered_user, password, error_message):
        pages.login_page.open()
        pages.login_page.login(registered_user["email"], password)
        assert pages.login_page.get_validation_error_message() == error_message
