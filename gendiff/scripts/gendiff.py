#!/usr/bin/env python3

from gendiff.parser_gendiff import to_parser_gendiff
from gendiff.gendiff import generate_diff


def main():
    args = to_parser_gendiff()
    diff = generate_diff(args.first_file, args.second_file, args.format)
    print(diff)


if __name__ == '__main__':
    main()
