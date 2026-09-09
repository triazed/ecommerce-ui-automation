from pages.base_ui import BaseUI
from config.urls import BASE_URL
import allure


class MainPage(BaseUI):
    URL = BASE_URL

    @allure.step("Open main page")
    def open(self):
        self.navigate_to(self.URL)