from selenium.common.exceptions import TimeoutException
from locators.components.header_locators import HeaderLocators
from pages.components.base_component import BaseComponent


class Header(BaseComponent):

    def click_register_button(self):
        self.click_element(HeaderLocators.REGISTER_BUTTON)

    def click_login_button(self):
        self.click_element(HeaderLocators.LOGIN_BUTTON)

    def click_logout_button(self):
        self.click_element(HeaderLocators.LOGOUT_BUTTON)

    def click_cart_button(self):
        self.click_element(HeaderLocators.CART_BUTTON)

    def click_close_notification_button(self):
        self.click_element(HeaderLocators.NOTIFICATION_CLOSE_BUTTON)

    def is_logout_button_visible(self):
        return self.is_element_visible(HeaderLocators.LOGOUT_BUTTON)

    def set_searched_value(self, text):
        self.set_text(HeaderLocators.SEARCH_INPUT, text)

    def click_search_button(self):
        self.click_element(HeaderLocators.SEARCH_BUTTON)

    def get_list_of_product_names_in_search_dropdown(self):
        try:
            return self.get_texts(HeaderLocators.SEARCH_DROPDOWN_PRODUCT_NAMES)
        except TimeoutException:
            return []

    def click_searched_product_in_search_dropdown(self, product_name):
        self.click_element(HeaderLocators.searched_product(product_name))


