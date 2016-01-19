from page.page_helper import InvalidUrl
from page.base import PageBase


class VimPlugins(PageBase):
    """Representing 'Vim Plugins' area"""

    def __init__(self, driver):
        super().__init__(driver, 'vim-plugin')
        self.driver = driver
        url = self.driver.current_url
        if not url.endswith('/#vim-plugin'):
            raise InvalidUrl('http://localhost:1234/#vim-plugin', url)
