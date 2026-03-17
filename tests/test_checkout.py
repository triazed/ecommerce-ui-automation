from config import urls
from test_data import expectations
from test_data import registration_data
from test_data import checkout_data

class TestCheckout:

    def test_guest_can_proceed_to_checkout_form(self, driver, pages, product_added_to_cart):
        pages.header.click_cart_button()
        pages.shopping_cart_page.click_terms_checkbox()
        pages.shopping_cart_page.click_checkout_button()
        pages.checkout_page.click_checkout_as_guest_button()
        assert pages.checkout_page.get_checkout_page_title() == expectations.CHECKOUT_PAGE_TITLE

    def test_authorized_user_can_proceed_to_checkout_form(self, driver, pages, product_added_to_cart):
        pages.base_page.navigate_to(urls.BASE_URL)
        pages.header.click_register_button()
        user = registration_data.new_user()
        pages.register_page.register(user['first_name'], user['last_name'], user['email'], user['password'])
        pages.header.click_cart_button()
        pages.shopping_cart_page.click_terms_checkbox()
        pages.shopping_cart_page.click_checkout_button()
        assert pages.checkout_page.get_checkout_page_title() == expectations.CHECKOUT_PAGE_TITLE

    def test_guest_checkout_successful(self, driver, pages, product_added_to_cart):
        pages.header.click_cart_button()
        pages.shopping_cart_page.click_terms_checkbox()
        pages.shopping_cart_page.click_checkout_button()
        pages.checkout_page.click_checkout_as_guest_button()
        product = product_added_to_cart
        user = registration_data.new_user()
        checkout_info = checkout_data.checkout_data()
        pages.checkout_page.set_billing_address_section(user['first_name'], user['last_name'], user['email'], checkout_info["country_name"], checkout_info["state_name"], checkout_info["city_name"], checkout_info["address_1"], checkout_info["zip_code"], checkout_info["phone_number"])
        pages.checkout_page.click_address_continue_button()
        pages.checkout_page.click_shipping_continue_button()
        pages.checkout_page.click_payment_continue_button()
        pages.checkout_page.click_payment_info_continue_button()
        assert product in pages.checkout_page.get_product_names_in_order_summary()
        pages.checkout_page.click_confirm_order_button()
        assert pages.checkout_page.get_order_completed_message() == expectations.ORDER_COMPLETED_MESSAGE
