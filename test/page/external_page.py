from page.page_helper import InvalidUrl
from page.base import PageBase


class ExternalPage(PageBase):
    """Representing external page"""

    def __init__(self, driver):
        super().__init__(driver, None)
        self.driver = driver
        url = self.driver.current_url
        if url.startswith('http://localhost'):
            raise InvalidUrl('external page url', url)

    def get_url(self):
        return self.driver.current_url

    def is_my_github_repo(self, name):
        return self.driver.current_url == ('https://github.com/rhysd/' + name)
