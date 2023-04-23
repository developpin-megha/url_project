import unittest

from input import *
from processor import *

logging.basicConfig(level=logging.DEBUG)

test_db = 'url_short_test.db'


class TestProcessor(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        override_database()

    def test_process(self):
        if Command == 'SHORTEN':
            assert True

    def test_check_url_regex(self):
        override_database()
        test_url = 'https://example.com'
        check_url_regex(test_url)
        assert (check_url_regex(test_url) is None)

    def test_generate_short_url(self):
        override_database()
        test_url = 'https://example.com'
        test_short_url = generate_short_url(test_url)
        assert test_short_url != test_url

    def test_get_short_url(self):
        override_database()
        test_url = 'https://example.com'
        test_short_url = get_short_url(test_url)
        assert test_short_url != test_url

    def test_long_url(self):
        override_database()
        test_url = 'https://example1.com'
        test_short_url = get_short_url(test_url)
        long_url = get_long_url(test_short_url)
        assert long_url == test_url

    @classmethod
    def tearDownClass(cls) -> None:
        close_connection_after_drop()


if __name__ == '__main__':
    unittest.main()
