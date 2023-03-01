def lower_bool(value):
    if value is False:
        value = 'false'
    elif value is True:
        value = 'true'
    elif value is None:
        value = 'null'
    elif isinstance(value, dict):
        for k, v in value.items():
            v = lower_bool(v)
    return value


def genetare_sorted_diff(file1, file2):
    keys1 = set(file1)
    keys2 = set(file2)
    all_keys = sorted(keys1.union(keys2))
    diff = {}
    for key in all_keys:
        if key in file1 and key not in file2:
            diff[key] = {'status': 'ONLY1', 'value': file1[key]}
        elif key in file2 and key not in file1:
            diff[key] = {'status': 'ONLY2', 'value': file2[key]}
        elif key in file2 and file1[key] == file2[key]:
            diff[key] = {'status': 'SAME', 'value': file1[key]}
        elif isinstance(file1[key], dict) and isinstance(file2[key], dict):
            diff_clild = genetare_sorted_diff(file1[key], file2[key])
            diff[key] = {'status': 'NESTED', 'value': diff_clild}
        else:
            diff[key] = {
                'status': 'DIFF',
                'value1': file1[key],
                'value2': file2[key]
            }
    return diff


def to_result_diff(diff):
    result = {}
    for key in diff:
        status = diff[key]['status']
        if status == 'ONLY1':
            valid_value = lower_bool(diff[key]['value'])
            new_key = f'- {key}'
            result[new_key] = valid_value
        elif status == 'ONLY2':
            valid_value = lower_bool(diff[key]['value'])
            new_key = f'+ {key}'
            result[new_key] = valid_value
        elif status == 'SAME':
            valid_value = lower_bool(diff[key]['value'])
            new_key = f'  {key}'
            result[new_key] = valid_value
        elif status == 'DIFF':
            valid_value1 = lower_bool(diff[key]['value1'])
            valid_value2 = lower_bool(diff[key]['value2'])
            new_key1 = f'- {key}'
            new_key2 = f'+ {key}'
            result[new_key1] = valid_value1
            result[new_key2] = valid_value2
        else:
            valid_value = diff[key]['value']
            new_key = f'  {key}'
            result[new_key] = to_result_diff(valid_value)
    return result
