from pages.base_page import BasePage
from pages.checkout_page import CheckoutPage
from pages.shopping_cart_page import ShoppingCartPage
from pages.components.header import Header
from pages.product_card_page import ProductCardPage
from pages.register_page import RegisterPage
from pages.login_page import LoginPage
from pages.search_results_page import SearchResultsPage


class PageFactory:
    def __init__(self, driver):
        self.driver = driver

    @property
    def base_page(self):
        return BasePage(self.driver)

    @property
    def header(self):
        return Header(self.driver)

    @property
    def register_page(self):
        return RegisterPage(self.driver)

    @property
    def login_page(self):
        return LoginPage(self.driver)

    @property
    def product_card_page(self):
        return ProductCardPage(self.driver)

    @property
    def search_results_page(self):
        return SearchResultsPage(self.driver)

    @property
    def shopping_cart_page(self):
        return ShoppingCartPage(self.driver)

    @property
    def checkout_page(self):
        return CheckoutPage(self.driver)
