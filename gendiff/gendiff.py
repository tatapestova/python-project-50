from gendiff.read_file import to_read_file
from gendiff.generate_diff import to_generate_sorted_diff
from gendiff.formatters.stylish import to_stylish
from gendiff.formatters.plain import to_plain
from gendiff.formatters.json import to_json


def choice_style(value, format):
    if format == 'plain':
        update_value = to_plain(value)
    elif format == 'json':
        update_value = to_json(value)
    else:
        update_value = to_stylish(value)
    return update_value


def generate_diff(first_file, second_file, format=to_stylish):
    file1 = to_read_file(first_file)
    file2 = to_read_file(second_file)
    diff = to_generate_sorted_diff(file1, file2)
    update_diff = choice_style(diff, format)
    return update_diff
