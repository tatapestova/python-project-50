from gendiff.file_editing.read_file import read_file
from gendiff.file_editing.generate_diff import genetare_sorted_diff
from gendiff.formatters.stylish import stylish
from gendiff.formatters.plain import plain


def choice_style(value, format):
    if format == 'plain':
        update_value = plain(value)
    else:
        update_value = stylish(value)
    return update_value


def generate_diff(first_file, second_file, format=stylish):
    file1 = read_file(first_file)
    file2 = read_file(second_file)
    diff = genetare_sorted_diff(file1, file2)
    update_diff = choice_style(diff, format)
    return update_diff
