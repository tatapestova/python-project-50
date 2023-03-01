import itertools


def stylish(value, replacer=' ', spaces_count=4):

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
