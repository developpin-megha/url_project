from input import Command
from data import *
import random
import logging

base_url = "www.developp.in/"


def generate_short_url(input_url, rand=random.randint(0, 9000)):
    import hashlib

    output = hashlib.md5((input_url + str(rand)).encode())
    hex_output = output.hexdigest()
    strip_hex_output = hex_output[7::-1]
    str_result = base_url + strip_hex_output
    return str_result


def process(inputs):
    result_url = None
    match inputs.command:
        case Command.EXPAND:
            result_url = get_long_url(inputs.url)
        case Command.SHORTEN:
            result_url = get_short_url(inputs.url)
        case Command.INITIALIZE:
            create_table()
    return result_url


def get_short_url(url):
    for i in range(0, 3):
        try:
            short_url = generate_short_url(url)
            insert_short_url(short_url, url)
            return short_url
        except Exception as ex:
            logging.error("Could not insert in try " + str(i) + ", trying again to insert " + url)
            logging.error("Exception " + str(ex))
            pass

    raise ValueError("Could not insert the URL in the database")
