from locators.shopping_cart_page_locators import ShoppingCartPageLocators
from pages.base_ui import BaseUI


class ShoppingCartPage(BaseUI):

    def get_product_names_in_cart(self):
        return self.get_texts(ShoppingCartPageLocators.PRODUCT_NAMES)

    def is_shopping_cart_empty(self):
        return self.is_element_invisible(ShoppingCartPageLocators.PRODUCTS_TABLE)

    def get_product_qty_in_cart(self, product_name):
        return int(self.get_element_attribute(ShoppingCartPageLocators.product_qty_in_cart(product_name), "value"))

    def remove_product_from_cart(self, product_name):
        self.click_element(ShoppingCartPageLocators.remove_product_button(product_name))

    def get_empty_cart_message(self):
        return self.get_text(ShoppingCartPageLocators.EMPTY_CART_MESSAGE)

    def click_terms_checkbox(self):
        self.click_element(ShoppingCartPageLocators.TERMS_CHECKBOX)

    def click_checkout_button(self):
        self.click_element(ShoppingCartPageLocators.CHECKOUT_BUTTON)

    def proceed_to_checkout_from_cart(self):
        self.click_terms_checkbox()
        self.click_checkout_button()
