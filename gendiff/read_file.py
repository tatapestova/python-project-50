import json
import yaml


def define_format(file):
    format = file.split('.')[-1]
    if format in ['yml', 'yaml', 'json']:
        return format
    else:
        raise ValueError('This file format is not supported.')


def parse_file(open_file, format):
    if format == 'json':
        result = json.load(open_file)
    elif format in ['yaml', 'yml']:
        result = yaml.safe_load(open_file)
    return result


def read_file(file):
    format = define_format(file)
    return parse_file(open(file), format)
