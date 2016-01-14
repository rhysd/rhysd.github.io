from page_helper import InvalidUrl
from external_page import ExternalPage


class Languages:
    """Representing 'Programming Language' area"""

    def __init__(self, driver):
        self.driver = driver
        url = self.driver.current_url
        if not url.endswith('/#language'):
            raise InvalidUrl('http://localhost/#language', url)

    def click_product_name(self, name):
        self.driver.find_element_by_link_text(name).click()
        return ExternalPage(self.driver)
