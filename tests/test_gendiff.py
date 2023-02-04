from gendiff.gendiff import read_file, genetare_sorted_dict_diff, to_style, lower_bool, generate_diff


def test_read_file():
    assert read_file('filepath1.json') == {
    "host": "hexlet.io",
    "timeout": 50,
    "proxy": "123.234.53.22",
    "follow": False
  }


def test_genetare_sorted_dict_diff():
    dict1 = {'a': 1, 'b': 2, 'c': 3}
    dict2 = {'a': 3, 'b': 2, 'd': 4}
    genetare_sorted_dict_diff(dict1, dict2) == {'a': 'diff', 'b': 'same', 'c': 'only1', 'd': 'only2'}


def test_to_style():
    diff_dict = {'a': 'diff', 'b': 'same', 'c': 'only1', 'd': 'only2'}
    dict1 = {'a': 1, 'b': 2, 'c': 3}
    dict2 = {'a': 3, 'b': 2, 'd': 4}
    to_style(diff_dict, dict1, dict2) == {' - a': 1, ' + a': 3, '  b': 2, ' - c': 3, ' + d': 4}


def test_lower_bool():
    dict1 = {
    "host": "hexlet.io",
    "timeout": 50,
    "proxy": "123.234.53.22",
    "follow": False
  }
    assert lower_bool(dict1) == {
    "host": "hexlet.io",
    "timeout": 50,
    "proxy": "123.234.53.22",
    "follow": 'false'
  }

def test_generate_diff():
    assert generate_diff('filepath1.json', 'filepath2.json') == '''{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}'''