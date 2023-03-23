from gendiff.read_file import read_file
from gendiff.generate_diff import generate_sorted_diff
from gendiff.formatters.stylish import to_stylish
from gendiff.formatters.plain import to_plain
from gendiff.formatters.json import to_json


def format_diff(value, format):
    if format == 'plain':
        update_value = to_plain(value)
    elif format == 'json':
        update_value = to_json(value)
    elif format == 'stylish':
        update_value = to_stylish(value)
    else:
        raise ValueError('''
        This format is not supported.
        Please, select one of this formats: 'stylish', 'plain', 'json'.
        ''')
    return update_value


def generate_diff(first_file, second_file, format=to_stylish):
    file1 = read_file(first_file)
    file2 = read_file(second_file)
    diff = generate_sorted_diff(file1, file2)
    update_diff = format_diff(diff, format)
    return update_diff
