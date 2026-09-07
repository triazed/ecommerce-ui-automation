from config import urls
from test_data import products
from test_data import expectations


class TestSearch:

    def test_search_product_by_keyword_via_dropdown(self, pages):
        pages.base_ui.navigate_to(urls.BASE_URL)
        pages.header.set_searched_value(products.SEARCHED_PRODUCT_BRAND)
        product_names_in_dropdown = pages.header.get_list_of_product_names_in_search_dropdown()
        assert product_names_in_dropdown
        for product_name in product_names_in_dropdown:
            assert products.SEARCHED_PRODUCT_BRAND in product_name

    def test_search_product_by_keyword_via_search_button(self, pages):
        pages.base_ui.navigate_to(urls.BASE_URL)
        pages.header.set_searched_value(products.SEARCHED_PRODUCT_BRAND)
        pages.header.click_search_button()
        product_names_in_search_results = pages.search_results_page.get_searched_products_names()
        assert product_names_in_search_results
        for product_name in product_names_in_search_results:
            assert products.SEARCHED_PRODUCT_BRAND in product_name

    def test_search_product_by_nonexistent_name_via_dropdown(self, pages):
        pages.base_ui.navigate_to(urls.BASE_URL)
        pages.header.set_searched_value(products.NONEXISTENT_PRODUCT_NAME)
        assert pages.header.is_search_dropdown_empty()

    def test_search_product_by_nonexistent_name_via_search_button(self, pages):
        pages.base_ui.navigate_to(urls.BASE_URL)
        pages.header.set_searched_value(products.NONEXISTENT_PRODUCT_NAME)
        pages.header.click_search_button()
        assert pages.search_results_page.get_no_result_message() == expectations.NO_RESULT_MESSAGE

    def test_navigate_to_product_page_from_link_in_dropdown(self, pages):
        pages.base_ui.navigate_to(urls.BASE_URL)
        pages.header.set_searched_value(products.SEARCHED_PRODUCT_NAME_QTY_1)
        pages.header.click_searched_product_in_search_dropdown(products.SEARCHED_PRODUCT_NAME_QTY_1)
        assert pages.product_card_page.get_product_name() == products.SEARCHED_PRODUCT_NAME_QTY_1

    def test_navigate_to_product_page_from_product_card_in_search_results(self, pages):
        pages.base_ui.navigate_to(urls.BASE_URL)
        pages.header.set_searched_value(products.SEARCHED_PRODUCT_NAME_QTY_1)
        pages.header.click_search_button()
        pages.search_results_page.click_searched_product_card(products.SEARCHED_PRODUCT_NAME_QTY_1)
        assert pages.product_card_page.get_product_name() == products.SEARCHED_PRODUCT_NAME_QTY_1
