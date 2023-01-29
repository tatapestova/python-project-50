import json


def lower_bool(dict_):
    for key, value in dict_.items():
        if value == False:
            dict_[key] = 'false'
        if value == True:
            dict_[key] = 'true'
    return dict_


def generate_diff(file1, file2):
    file1 = json.load(open(file1))
    file1 = dict(sorted(file1.items()))
    file2 = json.load(open(file2))
    file2 = dict(sorted(file2.items()))
    diff = {}
    
    for key in file1:
        if key in file2 and file1[key] == file2[key]:
            new_key = '  ' + key
            diff[new_key] = file1[key]
        if key in file2 and file1[key] != file2[key]:
            new_key = '- ' + key
            diff[new_key] = file1[key]
            new_key = '+ ' + key
            diff[new_key] = file2[key]
        if key not in file2:
            new_key = '- ' + key
            diff[new_key] = file1[key]
    
    set_diff = set(file2) - set(file1)
    for key in set_diff:
        new_key = '+ ' + key
        diff[new_key] = file2[key]
    
    lower_bool(diff)
    diff_str = '\n'.join([f'{key}: {value}' for key, value in diff.items()])
    result = '\n'.join(['{', diff_str, '}'])
    return result

