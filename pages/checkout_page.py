from locators.checkout_page_locators import CheckoutPageLocators
from pages.base_page import BasePage

class CheckoutPage(BasePage):

    def get_checkout_page_title(self):
        return self.get_text(CheckoutPageLocators.CHECKOUT_PAGE_TITLE)

    # Checkout or register section
    def click_checkout_as_guest_button(self):
        self.click_element(CheckoutPageLocators.CHECKOUT_AS_GUEST_BUTTON)

    # Billing address section
    def set_first_name(self, first_name):
        self.set_text(CheckoutPageLocators.FIRST_NAME, first_name)

    def set_last_name(self, last_name):
        self.set_text(CheckoutPageLocators.LAST_NAME, last_name)

    def set_email(self, email):
        self.set_text(CheckoutPageLocators.EMAIL, email)

    def click_countries_dropdown(self):
        self.click_element(CheckoutPageLocators.COUNTRIES_DROPDOWN)

    def choose_country(self, country_name):
        self.click_countries_dropdown()
        self.click_element(CheckoutPageLocators.country_name(country_name))

    def click_states_dropdown(self):
        self.click_element(CheckoutPageLocators.STATES_DROPDOWN)

    def choose_state(self, state_name):
        self.click_states_dropdown()
        self.click_element(CheckoutPageLocators.state_name(state_name))

    def set_city(self, city_name):
        self.set_text(CheckoutPageLocators.CITY, city_name)

    def set_address_1(self, address_1):
        self.set_text(CheckoutPageLocators.ADDRESS_1, address_1)

    def set_zip_code(self, zip_code):
        self.set_text(CheckoutPageLocators.ZIP_CODE, zip_code)

    def set_phone_number(self, phone_number):
        self.set_text(CheckoutPageLocators.PHONE, phone_number)

    def set_billing_address_section(self, first_name, last_name, email, country_name, state_name, city_name, address_1, zip_code, phone_number):
        self.set_first_name(first_name)
        self.set_last_name(last_name)
        self.set_email(email)
        self.choose_country(country_name)
        self.choose_state(state_name)
        self.set_city(city_name)
        self.set_address_1(address_1)
        self.set_zip_code(zip_code)
        self.set_phone_number(phone_number)

    def click_address_continue_button(self):
        self.click_element(CheckoutPageLocators.ADDRESS_CONTINUE_BUTTON)

    # Shipping method section
    def click_shipping_continue_button(self):
        self.click_element(CheckoutPageLocators.SHIPPING_CONTINUE_BUTTON)

    # Payment method section
    def click_payment_continue_button(self):
        self.click_element(CheckoutPageLocators.PAYMENT_METHOD_CONTINUE_BUTTON)

    # Payment information section
    def click_payment_info_continue_button(self):
        self.click_element(CheckoutPageLocators.PAYMENT_INFO_CONTINUE_BUTTON)

    # Confirm order section
    def get_product_names_in_order_summary(self):
        return self.get_texts(CheckoutPageLocators.PRODUCT_NAMES_IN_ORDER_SUMMARY)

    def click_confirm_order_button(self):
        self.click_element(CheckoutPageLocators.CONFIRM_ORDER_BUTTON)

    # Completed order section
    def get_order_completed_message(self):
        return self.get_text(CheckoutPageLocators.ORDER_COMPLETED_MESSAGE)
