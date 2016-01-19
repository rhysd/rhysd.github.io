from time import sleep


class PageBase:
    def __init__(self, driver, section_id):
        self.driver = driver
        self.section_id = section_id 

    def get_section_height(self):
        return self.driver.execute_script('return document.getElementById("{0}").offsetTop'.format(self.section_id))

    def wait_for_animation(self):
        sleep(3)  # XXX

