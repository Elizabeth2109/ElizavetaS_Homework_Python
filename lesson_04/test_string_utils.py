import pytest
from string_utils import StringUtils

string_utils = StringUtils()


# Тесты для метода capitalize (расширяем подсказку техлида)
@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
    ("a", "A"),
    ("123abc", "123abc"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("", ""),
    ("   ", "   "),
    ("\t\n", "\t\n"),
    (None, None),
])
def test_capitalize_negative(input_str, expected):
    if input_str is None:
        with pytest.raises((TypeError, AttributeError)):
            string_utils.capitalize(input_str)
    else:
        assert string_utils.capitalize(input_str) == expected


# Тесты для метода trim
@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("   skypro", "skypro"),
    ("    hello", "hello"),
    ("no_spaces", "no_spaces"),
    (" single", "single"),
    ("  multiple   spaces  ", "multiple   spaces"),  # пробелы внутри
    (" \t\n text \t\n ", "text"),  # смешанные пробелы
    ("   spaces  ", "spaces"),  # удаление всех пробелов
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("", ""),
    ("   ", ""),
    ("\t\ttext", "\t\ttext"),  # не удаляет табуляции
    ("text  ", "text  "),  # не удаляет пробелы в конце
    (None, None),  # None-вход
])
def test_trim_negative(input_str, expected):
    if input_str is None:
        with pytest.raises((TypeError, AttributeError)):
            string_utils.trim(input_str)
    else:
        assert string_utils.trim(input_str) == expected


# Тесты для метода contains
@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "S", True),
    ("SkyPro", "y", True),  # исправлено: "y" есть в "SkyPro"
    ("SkyPro", "o", True),
    ("test", "t", True),
])
def test_contains_positive(string, symbol, expected):
    assert string_utils.contains(string, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "U", False),
    ("SkyPro", "", False),  # пустой символ
    ("", "a", False),  # пустая строка
    ("abc", "d", False),
    (None, "a", False),  # None строка
    ("text", None, False),  # None символ
])
def test_contains_negative(string, symbol, expected):
    if string is None or symbol is None:
        with pytest.raises((TypeError, AttributeError)):
            string_utils.contains(string, symbol)
    else:
        assert string_utils.contains(string, symbol) == expected


# Тесты для метода delete_symbol
@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "k", "SyPro"),
    ("SkyPro", "Pro", "Sky"),
    ("ababab", "ab", ""),
    ("test", "x", "test"),  # символ отсутствует
    ("aaa", "a", ""),  # удаление всех символов
    ("mixedCase", "Case", "mixed"),  # регистр
    ("special@#$", "@#$", "special"),  # спецсимволы
    ("   spaces  ", " ", "spaces"),  # перенос из негативных: удаление пробелов
])
def test_delete_symbol_positive(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected", [
    ("", "a", ""),  # пустая строка
    ("text", "", "text"),  # пустой символ
    (None, "a", None),  # None строка
    ("text", None, "text"),  # None символ
])
def test_delete_symbol_negative(string, symbol, expected):
    if string is None or symbol is None:
        with pytest.raises((TypeError, AttributeError)):
            string_utils.delete_symbol(string, symbol)
    else:
        assert string_utils.delete_symbol(string, symbol) == expected
