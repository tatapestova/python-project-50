from gendiff.read_file import read_file
from gendiff.generate_diff import genetare_sorted_diff, to_result_diff
from gendiff.stylish import stylish


def generate_diff(first_file, second_file):
    file1 = read_file(first_file)
    file2 = read_file(second_file)
    diff = genetare_sorted_diff(file1, file2)
    new_diff = to_result_diff(diff)
    update_diff = stylish(new_diff)
    return update_diff
