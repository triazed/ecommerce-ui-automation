from test_data import products
from test_data import expectations
import allure


@allure.parent_suite("UI Tests")
@allure.suite("Search")
class TestSearch:

    @allure.feature("Search")
    @allure.story("Search for product via search dropdown")
    @allure.title("Matching products appear in the search dropdown")
    def test_search_product_by_keyword_via_dropdown(self, pages):
        pages.main_page.open()
        pages.header.set_searched_value(products.SEARCHED_PRODUCT_BRAND)
        product_names_in_dropdown = pages.header.get_list_of_product_names_in_search_dropdown()
        with allure.step("Verify matching products appear in the search dropdown"):
            assert product_names_in_dropdown
            for product_name in product_names_in_dropdown:
                assert products.SEARCHED_PRODUCT_BRAND in product_name

    @allure.feature("Search")
    @allure.story("Search for product via search results page")
    @allure.title("Matching products appear on the search results page")
    def test_search_product_by_keyword_via_search_button(self, pages):
        pages.main_page.open()
        pages.header.set_searched_value(products.SEARCHED_PRODUCT_BRAND)
        pages.header.click_search_button()
        product_names_in_search_results = pages.search_results_page.get_searched_products_names()
        with allure.step("Verify matching products appear on the search results page"):
            assert product_names_in_search_results
            for product_name in product_names_in_search_results:
                assert products.SEARCHED_PRODUCT_BRAND in product_name

    @allure.feature("Search")
    @allure.story("Search for non-existent product via search dropdown")
    @allure.title("Search for non-existent product shows no results in the search dropdown list")
    def test_search_product_by_nonexistent_name_via_dropdown(self, pages):
        pages.main_page.open()
        pages.header.set_searched_value(products.NONEXISTENT_PRODUCT_NAME)
        with allure.step("Verify no results in the search dropdown list"):
            assert pages.header.is_search_dropdown_empty()

    @allure.feature("Search")
    @allure.story("Search for non-existent product via search results page")
    @allure.title("Search for non-existent product shows no results on search results page")
    def test_search_product_by_nonexistent_name_via_search_button(self, pages):
        pages.main_page.open()
        pages.header.set_searched_value(products.NONEXISTENT_PRODUCT_NAME)
        pages.header.click_search_button()
        with allure.step("Verify no results on search results page"):
            assert pages.search_results_page.get_no_result_message() == expectations.NO_RESULT_MESSAGE

    @allure.feature("Search")
    @allure.story("Navigate to product page via search dropdown")
    @allure.title("User can open product page by clicking the product in the search dropdown")
    def test_navigate_to_product_page_from_link_in_dropdown(self, pages):
        pages.main_page.open()
        pages.header.set_searched_value(products.SEARCHED_PRODUCT_NAME)
        pages.header.click_searched_product_in_search_dropdown(products.SEARCHED_PRODUCT_NAME)
        with allure.step("Verify product page is open"):
            assert pages.product_card_page.get_product_name() == products.SEARCHED_PRODUCT_NAME

    @allure.feature("Search")
    @allure.story("Navigate to product page via search results page")
    @allure.title("User can open product page by clicking the product on the search results page")
    def test_navigate_to_product_page_from_product_card_in_search_results(self, pages):
        pages.main_page.open()
        pages.header.set_searched_value(products.SEARCHED_PRODUCT_NAME)
        pages.header.click_search_button()
        pages.search_results_page.click_searched_product_card(products.SEARCHED_PRODUCT_NAME)
        with allure.step("Verify product page is open"):
            assert pages.product_card_page.get_product_name() == products.SEARCHED_PRODUCT_NAME
