#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    pre_value = 0
    for numeral in reversed(roman_string):
        cur_value = roman_numerals.get(numeral, 0)
        if cur_value < pre_value:
            result -= cur_value
        else:
            result += cur_value
        pre_value = cur_value
    return result
