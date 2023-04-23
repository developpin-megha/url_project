import unittest

from input import *
from processor import *

logging.basicConfig(level=logging.DEBUG)


def test_process():
    if Command == 'SHORTEN':
        assert True


def test_check_url_regex():
    test_url = 'https://example.com'
    check_url_regex(test_url)
    assert (check_url_regex(test_url) is None)


def test_generate_short_url():
    test_url = 'https://example.com'
    test_short_url = generate_short_url(test_url)
    assert test_short_url != test_url


def test_get_short_url():
    test_url = 'https://example.com'
    test_short_url = get_short_url(test_url)
    assert test_short_url != test_url


def test_long_url():
    test_url = 'https://example1.com'
    test_short_url = get_short_url(test_url)
    long_url = get_long_url(test_short_url)
    assert long_url == test_url


if __name__ == '__main__':
    unittest.main()
