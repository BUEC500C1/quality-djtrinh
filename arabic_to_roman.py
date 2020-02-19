arabic_to_roman_pairs = [
    (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
    (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]

# Function to convert from arabic decimal to roman numeral
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
