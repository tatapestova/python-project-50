import json


def to_result_diff(diff):
    result = {}
    for key in diff:
        status = diff[key]['status']
        if status == 'ONLY1':
            valid_value = {
                'value': diff[key]['value'],
                'node status': 'REMOVED'
            }
            result[key] = valid_value
        elif status == 'ONLY2':
            valid_value = {
                'value': diff[key]['value'],
                'node status': 'ADDED'
            }
            result[key] = valid_value
        elif status == 'SAME':
            valid_value = {
                'value': diff[key]['value'],
                'node status': 'UNCHANGED'
            }
            result[key] = valid_value
        elif status == 'DIFF':
            valid_value = {
                'new value': diff[key]['value2'],
                'old value': diff[key]['value1'],
                'node status': 'UPDATED'
            }
            result[key] = valid_value
        else:
            node = diff[key]['value']
            valid_value = {
                'value': to_result_diff(node),
                'node status': 'NESTED'
            }
            result[key] = valid_value
    return result


def to_json(diff):
    update_diff = to_result_diff(diff)
    result = json.dumps(update_diff, indent=4)
    return result
