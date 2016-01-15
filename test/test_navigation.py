from selenium import webdriver
from page.main_page import MainPage


class TestNavigation:
    def setup_class(self):
        self.driver = webdriver.Chrome()

    def teardown_class(self):
        self.driver.quit()

    def setup_method(self, _):
        self.driver.get('http://localhost:1234')

    def get_current_height(self):
        return self.driver.execute_script('return document.body.scrollTop')

    def test_my_name_in_nav(self):
        main = MainPage(self.driver)
        assert main.click_my_name_in_nav().get_section_height() == self.get_current_height()
        assert main.active_item_is('top')

    def test_about_me_link(self):
        main = MainPage(self.driver)
        assert main.click_about_me_in_nav().get_section_height() == self.get_current_height()
        assert main.active_item_is('top')

    def test_language_link(self):
        main = MainPage(self.driver)
        height = main.click_languages_in_nav().get_section_height()
        assert abs(height - self.get_current_height()) < 3
        assert main.active_item_is('language')
