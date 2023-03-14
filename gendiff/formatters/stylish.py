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


def stylish(value, replacer=' ', spaces_count=4):  # noqa: C901
    def iter_(current_value, depth):
        if not isinstance(current_value, (list, dict)):
            return str(current_value)
        deep_indent_size1 = depth * spaces_count + 2
        deep_indent_size2 = depth * spaces_count + 4
        deep_indent1 = replacer * deep_indent_size1
        deep_indent2 = replacer * deep_indent_size2
        current_indent = replacer * (depth * spaces_count)
        lines = []
        if isinstance(current_value, dict):
            for k, v in current_value.items():
                lines.append(f'{deep_indent2}{k}: {iter_(v, depth + 1)}')
        for node in current_value:
            if 'status' in node:
                status = node['status']
                if status == 'DELETED':
                    value = lower_bool(node['value'])
                    new_key = '- ' + node['key']
                    lines.append(
                        f'{deep_indent1}{new_key}: {iter_(value, depth + 1)}'
                    )
                elif status == 'ADDED':
                    value = lower_bool(node['value'])
                    new_key = '+ ' + node['key']
                    lines.append(
                        f'{deep_indent1}{new_key}: {iter_(value, depth + 1)}'
                    )
                elif status == 'SAME':
                    value = lower_bool(node['value'])
                    new_key = '  ' + node['key']
                    lines.append(
                        f'{deep_indent1}{new_key}: {iter_(value, depth + 1)}'
                    )
                elif status == 'DIFF':
                    value1 = lower_bool(node['value1'])
                    value2 = lower_bool(node['value2'])
                    new_key1 = '- ' + node['key']
                    new_key2 = '+ ' + node['key']
                    lines.append(
                        f'{deep_indent1}{new_key1}: {iter_(value1, depth + 1)}'
                    )
                    lines.append(
                        f'{deep_indent1}{new_key2}: {iter_(value2, depth + 1)}'
                    )
                elif status == 'NESTED':
                    child = lower_bool(node['value'])
                    new_key = '  ' + node['key']
                    lines.append(
                        f'{deep_indent1}{new_key}: {iter_(child, depth + 1)}'
                    )
            else:
                pass
        result = itertools.chain("{", lines, [current_indent + "}"])
        return '\n'.join(result)
    return iter_(value, 0)
