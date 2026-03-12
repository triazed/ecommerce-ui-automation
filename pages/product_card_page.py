from locators.product_card_page_locators import ProductCardPageLocators
from pages.base_page import BasePage


class ProductCardPage(BasePage):

    def get_product_name(self):
        return self.get_text(ProductCardPageLocators.PRODUCT_NAME)

    def click_add_to_cart_button(self):
        self.click_element(ProductCardPageLocators.ADD_TO_CART_BUTTON)

    def get_min_quantity(self):
        if self.is_element_visible(ProductCardPageLocators.MIN_QUANTITY_NOTIFICATION):
            min_quantity = self.get_text(ProductCardPageLocators.MIN_QUANTITY_NOTIFICATION).removeprefix("This product has a minimum quantity of ")
            return min_quantity
        else:
            return "1"

    def set_add_to_cart_quantity(self):
        min_quantity = self.get_min_quantity()
        self.clear_and_set_text(ProductCardPageLocators.ADD_TO_CART_QUANTITY_INPUT, min_quantity)

    def add_product_to_cart(self):
        self.set_add_to_cart_quantity()
        self.click_add_to_cart_button()




