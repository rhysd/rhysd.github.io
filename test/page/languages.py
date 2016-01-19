from page.page_helper import InvalidUrl
from page.external_page import ExternalPage
from page.base import PageBase


class Languages(PageBase):
    """Representing 'Programming Language' area"""

    def __init__(self, driver):
        super().__init__(driver, 'language')
        self.driver = driver
        url = self.driver.current_url
        if not url.endswith('/#language'):
            raise InvalidUrl('http://localhost:1234/#language', url)

    def click_product_name(self, name):
        self.driver.find_element_by_link_text(name).click()
        self.wait_for_animation();
        return ExternalPage(self.driver)
