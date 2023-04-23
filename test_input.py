from python_url_project.code.input import check_url_regex


def test_check_url_regex():
    test_url = 'https://example.com'
    check_url_regex(test_url)
    assert (check_url_regex(test_url) is None)


def test_check_error_url_regex():
    test_url = 'https://example'
    try:
        check_url_regex(test_url)
    except ValueError:
        pass
    else:
        assert False


if __name__ == '__main__':
    test_check_url_regex()
    test_check_error_url_regex()
