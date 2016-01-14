class InvalidUrl(Exception):
    def __init__(self, expected, actual):
        self.expected = expected
        self.actual = actual

    def __repr__(self):
        return self.__str()

    def __str__(self):
        return 'Invalid URL: Expected {0} but actually {1}'.format(self.expected, self.actual)
