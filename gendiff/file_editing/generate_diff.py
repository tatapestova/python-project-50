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
