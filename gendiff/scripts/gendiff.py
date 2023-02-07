#!/usr/bin/env python3

from gendiff.parser_gendiff import parser_gendiff
from gendiff.gendiff import generate_diff


def main():
    args = parser_gendiff()
    diff = generate_diff(args.first_file, args.second_file)
    print(diff)


if __name__ == '__main__':
    main()
