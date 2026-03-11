from locators.product_card_page_locators import ProductCardPageLocators
from pages.base_page import BasePage


class ProductCardPage(BasePage):

    def get_product_name(self):
        return self.get_text(ProductCardPageLocators.PRODUCT_NAME)