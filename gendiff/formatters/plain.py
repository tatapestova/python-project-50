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


def is_complex_value(val):
    if isinstance(val, dict):
        val = '[complex value]'
    elif isinstance(val, int):
        val
    elif (val != 'false' and val != 'null' and val != 'true'):
        val = f"'{val}'"
    return val


def to_change_keys(value, prefix):
    if not isinstance(value, dict):
        return str(value)
    new_value = {}
    for k, v in value.items():
        new_key = f'{prefix}{k}'
        new_value[new_key] = v
    return new_value


def plain(diff, prefix=''):
    diff = to_change_keys(diff, prefix)
    result = []
    for key in diff:
        status = diff[key]['status']
        if status == 'DELETED':
            result.append(f"Property '{key}' was removed")
        elif status == 'ADDED':
            value = is_complex_value(lower_bool(diff[key]['value']))
            result.append(f"Property '{key}' was added with value: {value}")
        elif status == 'DIFF':
            value1 = is_complex_value(lower_bool(diff[key]['value1']))
            value2 = is_complex_value(lower_bool(diff[key]['value2']))
            result.append(
                f"Property '{key}' was updated. From {value1} to {value2}"
            )
        elif status == 'NESTED':
            value = diff[key]['value']
            result.append(plain(value, prefix=f'{key}.'))
    return '\n'.join(result)
