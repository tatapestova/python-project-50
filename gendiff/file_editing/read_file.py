import json
import yaml


def read_file(file):
    if '.json' in file:
        read_file = json.load(open(file))
    elif '.yml' or '.yaml' in file:
        read_file = yaml.safe_load(open(file))
    return read_file
