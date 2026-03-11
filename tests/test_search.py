from config import urls
from test_data import products
from test_data import expectations

class TestSearch:

    def test_search_product_by_name_via_dropdown(self, driver, pages):
        pages.base_page.navigate_to(urls.BASE_URL)
        pages.header.set_searched_value(products.SEARCHED_PRODUCT_NAME)
        pages.header.click_searched_product_in_search_dropdown(products.SEARCHED_PRODUCT_NAME)
        assert pages.product_card_page.get_product_name() == products.SEARCHED_PRODUCT_NAME

    def test_search_product_by_name_via_search_button(self, driver, pages):
        pages.base_page.navigate_to(urls.BASE_URL)
        pages.header.set_searched_value(products.SEARCHED_PRODUCT_NAME)
        pages.header.click_search_button()
        pages.search_results_page.click_searched_product(products.SEARCHED_PRODUCT_NAME)
        assert pages.product_card_page.get_product_name() == products.SEARCHED_PRODUCT_NAME

    def test_search_product_by_nonexistent_name_via_dropdown(self, driver, pages):
        pages.base_page.navigate_to(urls.BASE_URL)
        pages.header.set_searched_value(products.NONEXISTENT_PRODUCT_NAME)
        assert pages.header.get_list_of_product_names_in_search_dropdown() == []

    def test_search_product_by_nonexistent_name_via_search_button(self, driver, pages):
        pages.base_page.navigate_to(urls.BASE_URL)
        pages.header.set_searched_value(products.NONEXISTENT_PRODUCT_NAME)
        pages.header.click_search_button()
        assert pages.search_results_page.get_no_result_message() == expectations.NO_RESULT_MESSAGE


