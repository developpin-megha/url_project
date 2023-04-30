from enum import Enum
import logging


class Command(Enum):
    SHORTEN = 1
    EXPAND = 2
    INITIALIZE = 3


def check_url_regex(url):
    import re
    regex = ("((http|https)://)?(www.)?" +
             "[a-zA-Z0-9@:%._\\+~#?&//=]" +
             "{2,256}\\.[a-z]" +
             "{2,6}\\b([-a-zA-Z0-9@:%" +
             "._\\+~#?&//=]*)")

    # Compile the ReGex
    pattern = re.compile(regex)
    logging.info("checking the regex of the url")
    if not re.search(pattern, url):
        logging.error("invalid url " + url)
        raise ValueError("Invalid URL passed")


class Input:
    def __init__(self):
        self.command = Command.INITIALIZE
        self.url = None

    def get_inputs(self, args):
        self.url = args.url
        self.command = Command[args.command.upper()]
        if self.command == Command.EXPAND or self.command == Command.SHORTEN:
            assert self.url is not None
        if self.url is not None:
            check_url_regex(self.url)
        return self
