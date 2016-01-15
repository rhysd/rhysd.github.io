from page.external_page import ExternalPage
from page.page_helper import InvalidUrl
from page.base import PageBase


class Top(PageBase):
    """Representing 'About Me' area of main contents"""

    def __init__(self, driver):
        super().__init__(driver, 'top')
        self.driver = driver
        url = self.driver.current_url
        if not url.endswith('/#top'):
            raise InvalidUrl('http://localhost:1234/#top', url)

    def click_my_name(self):
        self.driver.find_element_by_css_selector('header h2 a').click()
        return ExternalPage(self.driver)

    def click_my_icon(self):
        self.driver.find_element_by_css_selector('header a').click()
        return None  # TODO
