import itertools


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


def to_result_diff(diff):
    result = {}
    for key in diff:
        status = diff[key]['status']
        if status == 'DELETED':
            valid_value = lower_bool(diff[key]['value'])
            new_key = f'- {key}'
            result[new_key] = valid_value
        elif status == 'ADDED':
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


def to_stylish(value, replacer=' ', spaces_count=4):

    def iter_(current_value, depth):
        if not isinstance(current_value, dict):
            return str(current_value)
        deep_indent_size1 = depth * spaces_count + 2
        deep_indent_size2 = depth * spaces_count + 4
        deep_indent1 = replacer * deep_indent_size1
        deep_indent2 = replacer * deep_indent_size2
        current_indent = replacer * (depth * spaces_count)
        lines = []
        for key, val in current_value.items():
            if '  ' in key or '+ ' in key or '- ' in key:
                lines.append(f'{deep_indent1}{key}: {iter_(val, depth + 1)}')
            else:
                lines.append(f'{deep_indent2}{key}: {iter_(val, depth + 1)}')
        result = itertools.chain("{", lines, [current_indent + "}"])
        return '\n'.join(result)

    return iter_(value, 0)


def stylish(diff):
    update_diff = to_result_diff(diff)
    result = to_stylish(update_diff)
    return result
