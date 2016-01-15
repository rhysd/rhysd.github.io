from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from page.top import Top
from page.languages import Languages
from page.base import PageBase
from page.desktop_apps import DesktopApps
from page.vim_plugins import VimPlugins


class MainPage(PageBase):
    """Representing left navigation area"""

    def __init__(self, driver):
        super().__init__(driver, 'main')
        self.driver = driver

    def wait_for_main_element(self):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.presence_of_element_located(
                (By.ID, 'intro')
            )
        )

    def click_my_name_in_nav(self):
        self.driver.find_element_by_css_selector('#title a').click()
        sleep(3)
        return Top(self.driver)

    def click_about_me_in_nav(self):
        self.driver.find_element_by_id('top-link').click()
        sleep(3)
        return Top(self.driver)

    def click_languages_in_nav(self):
        self.driver.find_element_by_id('language-link').click()
        sleep(3)
        return Languages(self.driver)

    def click_desktop_apps_in_nav(self):
        self.driver.find_element_by_id('desktop-app-link').click()
        sleep(3)
        return DesktopApps(self.driver)

    def click_vim_plugins_in_nav(self):
        self.driver.find_element_by_id('vim-plugin-link').click()
        sleep(3)
        return VimPlugins(self.driver)

    def active_item_is(self, name):
         item = self.driver.execute_script('return document.getElementById("' + name + '-link")')
         return 'active' in item.get_attribute('class')

