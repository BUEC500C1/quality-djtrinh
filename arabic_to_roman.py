import pytest


arabic_to_roman_pairs = [
    (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
    (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]


def arabic_to_roman(dec_input):
    roman_output = ""
    if type(dec_input) is not int:
        raise TypeError("Input must be a decimal input")
    elif(not 0 < dec_input < 4000):
        raise ValueError("Input must be between 0 and 4000")
    for pair in arabic_to_roman_pairs:
        count = dec_input//pair[0]  # how many multiples of each pair
        dec_input -= count * pair[0]  # subtract total pair value from input
        roman_output += (count * pair[1])  # concatenate number of roman numerals
    return roman_output


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
