from config import urls
from test_data import products
from test_data import expectations


class TestCart:

    def test_add_product_to_cart_from_product_card(self, driver, pages):
        pages.base_page.navigate_to(urls.BASE_URL)
        product = products.SEARCHED_PRODUCT_NAME_QTY_2
        pages.header.set_searched_value(product)
        pages.header.click_searched_product_in_search_dropdown(product)
        product_qty = pages.product_card_page.get_min_quantity()
        pages.product_card_page.add_product_to_cart()
        pages.header.click_close_notification_button()
        pages.header.click_cart_button()
        assert product in pages.shopping_cart_page.get_product_names_in_cart()
        assert pages.shopping_cart_page.get_product_qty_in_cart(product) == product_qty

    def test_add_product_to_cart_from_search_results(self, driver, pages):
        pages.base_page.navigate_to(urls.BASE_URL)
        product = products.SEARCHED_PRODUCT_NAME_QTY_1
        pages.header.set_searched_value(product)
        pages.header.click_search_button()
        pages.search_results_page.click_searched_product_add_to_cart_button(product)
        pages.header.click_close_notification_button()
        pages.header.click_cart_button()
        assert product in pages.shopping_cart_page.get_product_names_in_cart()
        assert pages.shopping_cart_page.get_product_qty_in_cart(product) == "1"

    def test_remove_product_from_cart(self, driver, pages):
        pages.base_page.navigate_to(urls.BASE_URL)
        product = products.SEARCHED_PRODUCT_NAME_QTY_1
        pages.header.set_searched_value(product)
        pages.header.click_search_button()
        pages.search_results_page.click_searched_product_add_to_cart_button(product)
        pages.header.click_close_notification_button()
        pages.header.click_cart_button()
        pages.shopping_cart_page.remove_product_from_cart(product)
        assert pages.shopping_cart_page.get_empty_cart_message() == expectations.EMPTY_CART_MESSAGE


