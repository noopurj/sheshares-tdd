roman_map = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}


def roman_to_arabic(roman_numeral):
    result = 0
    for i in range(0, len(roman_numeral)):
        current_char = roman_numeral[i]
        if i + 1 < len(roman_numeral):
            next_char = roman_numeral[i + 1]
            if roman_map[current_char] < roman_map[next_char]:
                result -= roman_map[current_char]
            else:
                result += roman_map[current_char]
        else:
            result += roman_map[current_char]

    return result


