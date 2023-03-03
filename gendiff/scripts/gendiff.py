#!/usr/bin/env python3

from gendiff.parser_gendiff import parser_gendiff
from gendiff.file_editing.gendiff import generate_diff


def main():
    args = parser_gendiff()
    diff = generate_diff(args.first_file, args.second_file, args.format)
    print(diff)


if __name__ == '__main__':
    main()
