import json


def form_result_diff(diff):
    result = {}
    for node in diff:
        status = node['status']
        key = node['key']
        if status == 'DELETED':
            valid_value = {
                'value': node['value'],
                'node status': 'REMOVED'
            }
            result[key] = valid_value
        elif status == 'ADDED':
            valid_value = {
                'value': node['value'],
                'node status': 'ADDED'
            }
            result[key] = valid_value
        elif status == 'SAME':
            valid_value = {
                'value': node['value'],
                'node status': 'UNCHANGED'
            }
            result[key] = valid_value
        elif status == 'DIFF':
            valid_value = {
                'new value': node['value2'],
                'old value': node['value1'],
                'node status': 'UPDATED'
            }
            result[key] = valid_value
        else:
            child = node['value']
            valid_value = {
                'value': form_result_diff(child),
                'node status': 'NESTED'
            }
            result[key] = valid_value
    return result


def to_json(diff):
    update_diff = form_result_diff(diff)
    result = json.dumps(update_diff, indent=4)
    return result
