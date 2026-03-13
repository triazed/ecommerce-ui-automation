import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import settings
from locators.components.header_locators import HeaderLocators
from locators.search_results_page_locators import SearchResultsPageLocators
from test_data import products
from config import urls
from pages.page_factory import PageFactory


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")

@pytest.fixture(scope="function")
def driver(request):
    browser = request.config.getoption("--browser").lower()
    if browser == "chrome":
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--window-size=1920x1080")
        driver = webdriver.Chrome(options=chrome_options)
    elif browser == "firefox":
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.add_argument("--window-size=1920x1080")
        driver = webdriver.Firefox(options=firefox_options)
    else:
        raise ValueError(f"{browser} not supported. Use chrome or firefox.")
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def pages(driver):
    return PageFactory(driver)

@pytest.fixture(scope="function")
def product_added_to_cart(driver):
    driver.get(urls.BASE_URL)
    product = products.SEARCHED_PRODUCT_NAME_QTY_1
    WebDriverWait(driver, settings.DEFAULT_TIMEOUT).until(EC.visibility_of_element_located(HeaderLocators.SEARCH_INPUT)).send_keys(product)
    WebDriverWait(driver, settings.DEFAULT_TIMEOUT).until(EC.element_to_be_clickable(HeaderLocators.SEARCH_BUTTON)).click()
    WebDriverWait(driver, settings.DEFAULT_TIMEOUT).until(EC.element_to_be_clickable(SearchResultsPageLocators.searched_product_add_to_cart_button(product))).click()
    WebDriverWait(driver, settings.DEFAULT_TIMEOUT).until(EC.element_to_be_clickable(HeaderLocators.NOTIFICATION_CLOSE_BUTTON)).click()
    return product

