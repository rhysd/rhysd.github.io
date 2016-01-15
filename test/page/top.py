from external_page import ExternalPage
from page_helper import InvalidUrl


class Top:
    """Representing 'About Me' area of main contents"""

    def __init__(self, driver):
        self.driver = driver
        url = self.driver.current_url
        if url != 'http://localhost:1234/':
            raise InvalidUrl('http://localhost:1234/', url)

    def current_height(self):
        return self.driver.execute_script('return document.body.scrollTop')

    def click_my_name(self):
        self.driver.find_element_by_css_selector('header h2 a').click()
        return ExternalPage(self.driver)

    def click_my_icon(self):
        self.driver.find_element_by_css_selector('header a').click()
        return None  # TODO
