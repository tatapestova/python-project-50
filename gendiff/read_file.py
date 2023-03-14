import json
import yaml


def read_file(file):
    if '.json' in file:
        format = 'json'
    elif '.yml' or '.yaml' in file:
        format = 'yaml'
    else:
        raise ValueError('This file format is not supported.')
    return parsing_file(open(file), format)


def parsing_file(open_file, format):
    if format in 'json':
        result = json.load(open_file)
    elif format in 'yaml':
        result = yaml.safe_load(open_file)
    return result
