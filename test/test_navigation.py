from selenium import webdriver
from page.main_page import MainPage


class TestNavigation:
    def setup_class(self):
        self.driver = webdriver.Chrome()

    def teardown_class(self):
        self.driver.quit()

    def setup_method(self, _):
        self.driver.get('http://localhost:1234')

    def test_my_name_in_nav(self):
        assert MainPage(self.driver).click_my_name_in_nav().current_height() == 0
