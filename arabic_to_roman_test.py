import pytest


def test_arabic_to_roman_float():
    with pytest.raises(TypeError):
        arabic_to_roman(3.14)


def test_arabic_to_roman_string():
    with pytest.raises(TypeError):
        arabic_to_roman("oinkies")


def test_arabic_to_roman_low_bound():
    with pytest.raises(ValueError):
        arabic_to_roman(0)


def test_arabic_to_roman_upper_bound():
    with pytest.raises(ValueError):
        arabic_to_roman(9000)


test_cases = [(1, "I"), (4, "IV"), (9, "IX"), (29, "XXIX"), (143, "CXLIII"),
              (1456, "MCDLVI"), (2775, "MMDCCLXXV"), (3714, "MMMDCCXIV")]


def test_arabic_to_roman():
    for num, rom in test_cases:
        assert arabic_to_roman(num) == rom
