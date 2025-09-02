import pytest
from string_utils import StringUtils


string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("   skypro", "skypro"),
    ("123", "123")
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("", ""),
    (" ", "")
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, input_sym, expected", [
    ("SkyPro", "S", True),
    ("SkyPro", "U", False),
    ("S", "S", True)
])
def test_contains_positive(input_str, input_sym, expected):
    assert string_utils.contains(input_str, input_sym) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, input_sym, expected", [
    ("", "U", False),
    (" ", "U", False)
])
def test_contains_negative(input_str, input_sym, expected):
    assert string_utils.contains(input_str, input_sym) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, input_sym, expected", [
    ("SkyPro", "k", "SyPro"),
    ("Sky Pro", "Pro", "Sky "),
    ("123", "3", "12")
])
def test_delete_symbol_positive(input_str, input_sym, expected):
    assert string_utils.delete_symbol(input_str, input_sym) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, input_sym, expected", [
    ("SlyPro", "k", "SlyPro"),
    ("", "Pro", ""),
    (" ", "Pro", " ")
])
def test_delete_symbol_negative(input_str, input_sym, expected):
    assert string_utils.delete_symbol(input_str, input_sym) == expected
