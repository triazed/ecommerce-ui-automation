from config import urls
from test_data.registration_data import new_user
from test_data.expectations import (REGISTRATION_RESULT_SUCCESS_MESSAGE, EMAIL_EXISTS_ERROR_MESSAGE)

class TestRegister:

    def test_successful_registration(self, driver, pages):
        pages.base_page.navigate_to(urls.BASE_URL)
        pages.header.click_register_button()
        user = new_user()
        pages.register_page.register(user['first_name'], user['last_name'], user['email'], user['password'])
        assert pages.register_page.get_registration_result_message() == REGISTRATION_RESULT_SUCCESS_MESSAGE
        assert pages.header.is_logout_button_visible()

    def test_registration_with_existing_email(self, driver, pages):
        pages.register_page.open()
        user = new_user()
        pages.register_page.register(user['first_name'], user['last_name'], user['email'], user['password'])
        pages.header.click_logout_button()
        pages.register_page.open()
        pages.register_page.register(user['first_name'], user['last_name'], user['email'], user['password'])
        assert pages.register_page.get_validation_error_message() == EMAIL_EXISTS_ERROR_MESSAGE
        assert not pages.header.is_logout_button_visible()
