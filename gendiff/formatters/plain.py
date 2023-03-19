def to_correct_value(val):
    if isinstance(val, dict):
        val = '[complex value]'
    elif val is False:
        val = 'false'
    elif val is True:
        val = 'true'
    elif val is None:
        val = 'null'
    elif isinstance(val, int):
        val
    else:
        val = f"'{val}'"
    return val


def to_plain(diff, path=''):
    result = []
    for node in diff:
        status = node['status']
        if status == 'DELETED':
            result.append(f"Property '{path}{node['key']}' was removed")
        elif status == 'ADDED':
            val = to_correct_value(node['value'])
            result.append(
                f"Property '{path}{node['key']}' was added with value: {val}"
            )
        elif status == 'DIFF':
            val1 = to_correct_value(node['value1'])
            val2 = to_correct_value(node['value2'])
            key = node['key']
            result.append(
                f"Property '{path}{key}' was updated. From {val1} to {val2}"
            )
        elif status == 'NESTED':
            child = node['value']
            key_child = node['key']
            result.append(to_plain(child, path=path + f'{key_child}.'))
    return '\n'.join(result)
