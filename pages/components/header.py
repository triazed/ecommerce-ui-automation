from locators.components.header_locators import HeaderLocators
from pages.base_ui import BaseUI
import allure


class Header(BaseUI):

    def click_register_button(self):
        self.click_element(HeaderLocators.REGISTER_BUTTON)

    def click_login_button(self):
        self.click_element(HeaderLocators.LOGIN_BUTTON)

    def click_logout_button(self):
        self.click_element(HeaderLocators.LOGOUT_BUTTON)

    @allure.step("Open shopping cart")
    def click_cart_button(self):
        self.click_element(HeaderLocators.CART_BUTTON)

    @allure.step("Close notification message")
    def click_close_notification_button(self):
        self.click_element(HeaderLocators.NOTIFICATION_CLOSE_BUTTON)

    def is_logout_button_visible(self):
        return self.is_element_visible(HeaderLocators.LOGOUT_BUTTON)

    @allure.step("Fill in searched keyword")
    def set_searched_value(self, text):
        self.set_text(HeaderLocators.SEARCH_INPUT, text)

    @allure.step("Click search button")
    def click_search_button(self):
        self.click_element(HeaderLocators.SEARCH_BUTTON)

    @allure.step("Get list of products in search dropdown")
    def get_list_of_product_names_in_search_dropdown(self):
        return self.get_texts(HeaderLocators.SEARCH_DROPDOWN_PRODUCT_NAMES)

    def is_search_dropdown_empty(self):
        return self.is_element_invisible(HeaderLocators.SEARCH_DROPDOWN_CONTENT)

    allure.step("Click product name in search dropdown")
    def click_searched_product_in_search_dropdown(self, product_name):
        self.click_element(HeaderLocators.searched_product(product_name))
