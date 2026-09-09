from locators.product_card_page_locators import ProductCardPageLocators
from pages.base_ui import BaseUI
import allure


class ProductCardPage(BaseUI):

    def get_product_name(self):
        return self.get_text(ProductCardPageLocators.PRODUCT_NAME)

    def click_add_to_cart_button(self):
        self.click_element(ProductCardPageLocators.ADD_TO_CART_BUTTON)

    @allure.step("Add product to cart")
    def add_product_to_cart(self):
        self.click_add_to_cart_button()
