import pytest


from gendiff.gendiff import generate_diff


FLAT_JSON1 = 'tests/fixtures/files/filepath1.json'
FLAT_JSON2 = 'tests/fixtures/files/filepath2.json'
FLAT_YML1 = 'tests/fixtures/files/filepath1.yml'
FLAT_YAML2 = 'tests/fixtures/files/filepath2.yaml'
NESTED_JSON1 = 'tests/fixtures/files/file1.json'
NESTED_JSON2 = 'tests/fixtures/files/file2.json'
NESTED_YML1 = 'tests/fixtures/files/file1.yml'
NESTED_YAML2 = 'tests/fixtures/files/file2.yaml'

STYLISH_FLAT = 'tests/fixtures/results/slylish_flat.txt'
STYLISH_NESTED = 'tests/fixtures/results/stylish_nested.txt'
PLAIN_NESTED = 'tests/fixtures/results/plain_nested.txt'
PLAIN_FLAT = 'tests/fixtures/results/plain_flat.txt'
JSON_NESTED = 'tests/fixtures/results/json_nested.txt'
JSON_FLAT = 'tests/fixtures/results/json_flat.txt'

@pytest.mark.parametrize('file1, file2, stile, expected', [
    (FLAT_JSON1, FLAT_JSON2, 'stylish', STYLISH_FLAT),
    (FLAT_YML1, FLAT_YAML2, 'stylish', STYLISH_FLAT), 
    (FLAT_JSON1, FLAT_YAML2, 'stylish', STYLISH_FLAT),
    (NESTED_JSON1, NESTED_JSON2, 'stylish', STYLISH_NESTED),
    (NESTED_YML1, NESTED_YAML2, 'stylish', STYLISH_NESTED),
    (NESTED_JSON1, NESTED_YAML2, 'stylish', STYLISH_NESTED),
    (FLAT_JSON1, FLAT_JSON2, 'plain', PLAIN_FLAT),
    (FLAT_YML1, FLAT_YAML2, 'plain', PLAIN_FLAT),
    (FLAT_JSON1, FLAT_YAML2, 'plain', PLAIN_FLAT),
    (NESTED_JSON1, NESTED_JSON2, 'plain', PLAIN_NESTED),
    (NESTED_YML1, NESTED_YAML2, 'plain', PLAIN_NESTED),
    (NESTED_JSON1, NESTED_YAML2, 'plain', PLAIN_NESTED),
    (FLAT_JSON1, FLAT_JSON2, 'json', JSON_FLAT),
    (FLAT_YML1, FLAT_YAML2, 'json', JSON_FLAT),
    (FLAT_JSON1, FLAT_YAML2, 'json', JSON_FLAT),
    (NESTED_JSON1, NESTED_JSON2, 'json', JSON_NESTED),
    (NESTED_YML1, NESTED_YAML2, 'json', JSON_NESTED),
    (NESTED_JSON1, NESTED_YAML2, 'json', JSON_NESTED)
])
def test_generate_diff(file1, file2, stile, expected):
    with open(expected) as file:
        expected_result = file.read()
    assert generate_diff(file1, file2, stile) == expected_result
