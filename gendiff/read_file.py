import json
import yaml


def to_define_format(file):
    format = file.split('.')[-1]
    if 'yml' or 'yaml' or 'json' == format:
        return format
    else:
        raise ValueError('This file format is not supported.')


def to_parsing_file(open_file, format):
    if format == 'json':
        result = json.load(open_file)
    elif format == 'yaml' or 'yml':
        result = yaml.safe_load(open_file)
    return result


def to_read_file(file):
    format = to_define_format(file)
    return to_parsing_file(open(file), format)
