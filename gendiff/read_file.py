import json
import yaml


def open_file(file):
    if '.json' in file:
        format = 'json'
    elif '.yml' or '.yaml' in file:
        format = 'yaml'
    else:
        raise ValueError('This file format is not supported.')
    return open(file), format


def read_file(file):
    read_file, format = open_file(file)
    if format in 'json':
        result = json.load(read_file)
    elif format in 'yaml':
        result = yaml.safe_load(read_file)
    return result
