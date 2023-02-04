import json


def read_file(file):
    read_file = json.load(open(file))
    return read_file


def genetare_sorted_dict_diff(file1, file2):
    diff = {}
    for key in file1:
        if key in file2 and file1[key] == file2[key]:
            diff[key] = 'same'
        if key in file2 and file1[key] != file2[key]:
            diff[key] = 'diff'
        if key not in file2:
            diff[key] = 'only1'
    set_diff = set(file2) - set(file1)
    for key in set_diff:
        diff[key] = 'only2'
    sorted_diff = dict(sorted(diff.items()))
    return sorted_diff


def to_style(diff_dict, dict1, dict2):
    result = {}
    for key, value in diff_dict.items():
        if value == 'same':
            new_key = '   ' + key
            result[new_key] = dict1[key]
        if value == 'diff':
            new_key = ' - ' + key
            result[new_key] = dict1[key]
            new_key = ' + ' + key
            result[new_key] = dict2[key]
        if value == 'only1':
            new_key = ' - ' + key
            result[new_key] = dict1[key]
        if value == 'only2':
            new_key = ' + ' + key
            result[new_key] = dict2[key]
    return result


def lower_bool(dict_):
    for key, value in dict_.items():
        if value is False:
            dict_[key] = 'false'
        if value is True:
            dict_[key] = 'true'
    return dict_


def generate_diff(first_file: dict, second_file: dict):
    file1 = read_file(first_file)
    file2 = read_file(second_file)
    diff = genetare_sorted_dict_diff(file1, file2)
    update_diff = to_style(diff, file1, file2)
    lower_bool(update_diff)
    diff_str = '\n'.join([f'{key}: {value}' for key, value in update_diff.items()])
    result = '\n'.join(['{', diff_str, '}'])
    return result


__all__ = ('read_file', 'genetare_sorted_dict_diff', 'to_style', 'lower_bool', 'generate_diff')
