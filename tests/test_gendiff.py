from gendiff.file_editing.gendiff import generate_diff


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

def test_generate_stylish_flat_diff():
    with open(STYLISH_FLAT) as file:
        expected_flat_result = file.read()
    assert generate_diff(FLAT_JSON1, FLAT_JSON2) == expected_flat_result
    assert generate_diff(FLAT_YML1, FLAT_YAML2) == expected_flat_result
    assert generate_diff(FLAT_JSON1, FLAT_YAML2) == expected_flat_result


def test_generate_stylish_nested_diff():
    with open(STYLISH_NESTED) as file:
        expected_nested_result = file.read()
    assert generate_diff(NESTED_JSON1, NESTED_JSON2) == expected_nested_result
    assert generate_diff(NESTED_YML1, NESTED_YAML2) == expected_nested_result
    assert generate_diff(NESTED_JSON1, NESTED_YAML2) == expected_nested_result

def test_generate_flat_nested_diff():
    with open(PLAIN_FLAT) as file:
        expected_flat_result = file.read()
    assert generate_diff(FLAT_JSON1, FLAT_JSON2, 'plain') == expected_flat_result
    assert generate_diff(FLAT_YML1, FLAT_YAML2, 'plain') == expected_flat_result
    assert generate_diff(FLAT_JSON1, FLAT_YAML2, 'plain') == expected_flat_result


def test_generate_plain_nested_diff():
    with open(PLAIN_NESTED) as file:
        expected_nested_result = file.read()
    assert generate_diff(NESTED_JSON1, NESTED_JSON2, 'plain') == expected_nested_result
    assert generate_diff(NESTED_YML1, NESTED_YAML2, 'plain') == expected_nested_result
    assert generate_diff(NESTED_JSON1, NESTED_YAML2, 'plain') == expected_nested_result


def test_generate_json_nested_diff():
    with open(JSON_FLAT) as file:
        expected_flat_result = file.read()
    assert generate_diff(FLAT_JSON1, FLAT_JSON2, 'json') == expected_flat_result
    assert generate_diff(FLAT_YML1, FLAT_YAML2, 'json') == expected_flat_result
    assert generate_diff(FLAT_JSON1, FLAT_YAML2, 'json') == expected_flat_result


def test_generate_json_nested_diff():
    with open(JSON_NESTED) as file:
        expected_nested_result = file.read()
    assert generate_diff(NESTED_JSON1, NESTED_JSON2, 'json') == expected_nested_result
    assert generate_diff(NESTED_YML1, NESTED_YAML2, 'json') == expected_nested_result
    assert generate_diff(NESTED_JSON1, NESTED_YAML2, 'json') == expected_nested_result
