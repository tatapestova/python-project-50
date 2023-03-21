def generate_sorted_diff(file1, file2):
    keys1 = set(file1)
    keys2 = set(file2)
    all_keys = sorted(keys1.union(keys2))
    diff = []
    for key in all_keys:
        if key in file1 and key not in file2:
            node = {
                'key': key,
                'status': 'DELETED',
                'value': file1[key]
            }
            diff.append(node)
        elif key in file2 and key not in file1:
            node = {
                'key': key,
                'status': 'ADDED',
                'value': file2[key]
            }
            diff.append(node)
        elif file1[key] == file2[key]:
            node = {
                'key': key,
                'status': 'SAME',
                'value': file1[key]
            }
            diff.append(node)
        elif isinstance(file1[key], dict) and isinstance(file2[key], dict):
            diff_clild = generate_sorted_diff(file1[key], file2[key])
            node = {
                'key': key,
                'status': 'NESTED',
                'value': diff_clild
            }
            diff.append(node)
        else:
            node = {
                'key': key,
                'status': 'DIFF',
                'value1': file1[key],
                'value2': file2[key]
            }
            diff.append(node)
    return diff
