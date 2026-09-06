from locators.checkout_page_locators import CheckoutPageLocators
from pages.base_ui import BaseUI


class CheckoutPage(BaseUI):

    def get_checkout_page_title(self):
        return self.get_text(CheckoutPageLocators.CHECKOUT_PAGE_TITLE)

    # Checkout or register section
    def click_checkout_as_guest_button(self):
        self.click_element(CheckoutPageLocators.CHECKOUT_AS_GUEST_BUTTON)

    # Billing address section
    def set_first_name(self, checkout_data):
        self.set_text(CheckoutPageLocators.FIRST_NAME, checkout_data["first_name"])

    def set_last_name(self, checkout_data):
        self.set_text(CheckoutPageLocators.LAST_NAME, checkout_data["last_name"])

    def set_email(self, checkout_data):
        self.set_text(CheckoutPageLocators.EMAIL, checkout_data["email"])

    def choose_country(self, checkout_data):
        country_name = checkout_data["country_name"]
        self.select_from_dropdown_by_visible_text(CheckoutPageLocators.COUNTRIES_DROPDOWN, country_name)

    def choose_state(self, checkout_data):
        state_name = checkout_data["state_name"]
        self.select_from_dropdown_by_visible_text(CheckoutPageLocators.STATES_DROPDOWN, state_name)

    def set_city(self, checkout_data):
        self.set_text(CheckoutPageLocators.CITY, checkout_data["city_name"])

    def set_address_1(self, checkout_data):
        self.set_text(CheckoutPageLocators.ADDRESS_1, checkout_data["address_1"])

    def set_zip_code(self, checkout_data):
        self.set_text(CheckoutPageLocators.ZIP_CODE, checkout_data["zip_code"])

    def set_phone_number(self, checkout_data):
        self.set_text(CheckoutPageLocators.PHONE, checkout_data["phone_number"])

    def set_billing_address_section(self, checkout_data):
        self.set_first_name(checkout_data)
        self.set_last_name(checkout_data)
        self.set_email(checkout_data)
        self.choose_country(checkout_data)
        self.choose_state(checkout_data)
        self.set_city(checkout_data)
        self.set_address_1(checkout_data)
        self.set_zip_code(checkout_data)
        self.set_phone_number(checkout_data)

    def continue_from_billing_address_section(self):
        self.click_element(CheckoutPageLocators.ADDRESS_CONTINUE_BUTTON)

    # Shipping method section
    def continue_from_shipping_method_section(self):
        self.click_element(CheckoutPageLocators.SHIPPING_METHOD_CONTINUE_BUTTON)

    # Payment method section
    def continue_from_payment_method_section(self):
        self.click_element(CheckoutPageLocators.PAYMENT_METHOD_CONTINUE_BUTTON)

    # Payment information section
    def continue_from_payment_info_section(self):
        self.click_element(CheckoutPageLocators.PAYMENT_INFO_CONTINUE_BUTTON)

    # Confirm order section
    def get_product_names_in_order_summary(self):
        return self.get_texts(CheckoutPageLocators.PRODUCT_NAMES_IN_ORDER_SUMMARY)

    def click_confirm_order_button(self):
        self.click_element(CheckoutPageLocators.CONFIRM_ORDER_BUTTON)

    # Completed order section
    def get_order_completed_message(self):
        return self.get_text(CheckoutPageLocators.ORDER_COMPLETED_MESSAGE)
