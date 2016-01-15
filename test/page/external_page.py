from page_helper import InvalidUrl


class ExternalPage:
    """Representing external page"""

    def __init__(self, driver):
        self.driver = driver
        url = self.driver.current_url
        if url.startswith('http://localhost'):
            raise InvalidUrl('external page url', url)

    def get_url(self):
        return self.driver.current_url

    def is_my_github_repo(self, name):
        return self.driver.current_url == ('https://github.com/rhysd/' + name)
