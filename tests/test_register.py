from config import urls
from test_data.registration_data import new_user
from test_data.expectations import REGISTRATION_RESULT_SUCCESS_MESSAGE

class TestRegister:

    def test_register(self, driver, pages):
        pages.base_page.navigate_to(urls.BASE_URL)
        pages.header.click_register_button()
        user = new_user()
        pages.register_page.register(user['first_name'], user['last_name'], user['email'], user['password'])
        assert pages.register_page.get_registration_result_message() == REGISTRATION_RESULT_SUCCESS_MESSAGE
        assert pages.header.is_logout_button_visible()
