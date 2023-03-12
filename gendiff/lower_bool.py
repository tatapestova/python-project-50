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
