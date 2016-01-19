from page.page_helper import InvalidUrl
from page.base import PageBase


class DesktopApps(PageBase):
    """Representing 'Desktop Applications' area"""

    def __init__(self, driver):
        super().__init__(driver, 'desktop-app')
        self.driver = driver
        url = self.driver.current_url
        if not url.endswith('/#desktop-app'):
            raise InvalidUrl('http://localhost:1234/#desktop-app', url)

