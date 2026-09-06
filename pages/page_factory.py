from pages.base_ui import BaseUI
from pages.checkout_page import CheckoutPage
from pages.shopping_cart_page import ShoppingCartPage
from pages.components.header import Header
from pages.product_card_page import ProductCardPage
from pages.register_page import RegisterPage
from pages.login_page import LoginPage
from pages.search_results_page import SearchResultsPage


class PageFactory:
    def __init__(self, driver):
        self.base_ui = BaseUI(driver)
        self.header = Header(driver)
        self.checkout_page = CheckoutPage(driver)
        self.login_page = LoginPage(driver)
        self.product_card_page = ProductCardPage(driver)
        self.register_page = RegisterPage(driver)
        self.search_results_page = SearchResultsPage(driver)
        self.shopping_cart_page = ShoppingCartPage(driver)
