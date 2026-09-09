from test_data import products
from test_data import expectations
import allure


@allure.parent_suite("UI Tests")
@allure.suite("Shopping cart")
class TestCart:

    @allure.feature("Shopping cart")
    @allure.story("Add product to cart from product page")
    @allure.title("Product can be added to cart from the product page")
    def test_add_product_to_cart_from_product_page(self, pages):
        pages.main_page.open()
        product = products.SEARCHED_PRODUCT_NAME
        pages.header.set_searched_value(product)
        pages.header.click_searched_product_in_search_dropdown(product)
        pages.product_card_page.add_product_to_cart()
        pages.header.click_close_notification_button()
        pages.header.click_cart_button()
        product_names_in_cart = pages.shopping_cart_page.get_product_names_in_cart()
        with allure.step("Verify the expected product is present in the cart"):
            assert len(product_names_in_cart) == 1
            assert product in product_names_in_cart
            assert pages.shopping_cart_page.get_product_qty_in_cart(product) == 1

    @allure.feature("Shopping cart")
    @allure.story("Add product to cart from search results page")
    @allure.title("Product can be added to cart from search results page")
    def test_add_product_to_cart_from_search_results(self, pages):
        pages.main_page.open()
        product = products.SEARCHED_PRODUCT_NAME
        pages.header.set_searched_value(product)
        pages.header.click_search_button()
        pages.search_results_page.click_searched_product_add_to_cart_button(product)
        pages.header.click_close_notification_button()
        pages.header.click_cart_button()
        product_names_in_cart = pages.shopping_cart_page.get_product_names_in_cart()
        with allure.step("Verify the expected product is present in the cart"):
            assert len(product_names_in_cart) == 1
            assert product in product_names_in_cart
            assert pages.shopping_cart_page.get_product_qty_in_cart(product) == 1

    @allure.feature("Shopping cart")
    @allure.story("Removing product from cart")
    @allure.title("Product can be removed from cart")
    def test_remove_product_from_cart(self, pages, product_added_to_cart):
        pages.header.click_cart_button()
        product = product_added_to_cart
        pages.shopping_cart_page.remove_product_from_cart(product)
        with allure.step("Verify the cart is empty"):
            assert pages.shopping_cart_page.is_shopping_cart_empty()
            assert pages.shopping_cart_page.get_empty_cart_message() == expectations.EMPTY_CART_MESSAGE
