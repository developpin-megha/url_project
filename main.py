import argparse
from code.processor import process
from code.input import Input
import logging

logging.basicConfig(level=logging.DEBUG)


def main():
    parser = argparse.ArgumentParser(description='URL shortener')
    parser.add_argument('-c', '--command', '-command', required=True, help="Command/Action")
    parser.add_argument('-u', '--url', '-url', required=False, help="URL for action")
    args = parser.parse_args()
    inputs = Input().get_inputs(args)
    url = process(inputs)
    print(url)


if __name__ == "__main__":
    main()
