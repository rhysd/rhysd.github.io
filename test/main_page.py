from top import Top
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class MainPage:
    """Representing left navigation area"""

    def __init__(self, driver):
        self.driver = driver

    def wait_for_main_element(self):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.presence_of_element_located(
                (By.ID, 'intro')
            )
        )

    def click_my_name_in_nav(self):
        self.driver.find_element_by_css_selector('#title a').click()
        self.wait_for_main_element()
        return Top(self.driver)

    def click_about_me_in_nav(self):
        self.driver.find_element_by_id('top-link').click()
        return Top(self.driver)
