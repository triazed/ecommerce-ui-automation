from config.urls import BASE_URL
from test_data.registration_data import new_user
from test_data.expectations import CUSTOMER_NOT_FOUND_ERROR_MESSAGE

class TestLogin:

    def test_successful_login(self, driver, pages, registered_user):
        pages.base_page.navigate_to(BASE_URL)
        pages.header.click_login_button()
        user_email, user_password = registered_user["email"], registered_user["password"]
        pages.login_page.login(user_email, user_password)
        assert pages.header.is_logout_button_visible()

    def test_login_with_unregistered_email(self, driver, pages):
        pages.login_page.open()
        user = new_user()
        pages.login_page.login(user['email'], user['password'])
        assert pages.login_page.get_validation_error_message() == CUSTOMER_NOT_FOUND_ERROR_MESSAGE
