from gendiff.gendiff import generate_diff


PLAIN_JSON1 = 'tests/fixtures/files/filepath1.json'
PLAIN_JSON2 = 'tests/fixtures/files/filepath2.json'
PLAIN_YML1 = 'tests/fixtures/files/filepath1.yml'
PLAIN_YML2 = 'tests/fixtures/files/filepath2.yml'
NESTED_JSON1 = 'tests/fixtures/files/file1.json'
NESTED_JSON2 = 'tests/fixtures/files/file2.json'
NESTED_YML1 = 'tests/fixtures/files/file1.yml'
NESTED_YML2 = 'tests/fixtures/files/file2.yml'

RESULT_PLAIN = 'tests/fixtures/result_plain.txt'
RESULT_NESTED = 'tests/fixtures/result_nested.txt'


def test_generate_plain_diff():
    with open(RESULT_PLAIN) as file:
        expected_plain_result = file.read()
    assert generate_diff(PLAIN_JSON1, PLAIN_JSON2) == expected_plain_result
    assert generate_diff(PLAIN_YML1, PLAIN_YML2) == expected_plain_result


def test_generate_nested_diff():
    with open(RESULT_NESTED) as file:
        expected_nested_result = file.read()
    assert generate_diff(NESTED_JSON1, NESTED_JSON2) == expected_nested_result
    assert generate_diff(NESTED_YML1, NESTED_YML2) == expected_nested_result