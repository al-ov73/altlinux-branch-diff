import argparse

from generate_diff.parser import parse_url


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    args = parser.parse_args()
    diff = parse_url()


if __name__ == '__main__':
    main()