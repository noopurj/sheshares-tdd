mapping = {
    1: 'I',
    4: 'IV',
    5: 'V',
    9: 'IX',
    10: 'X'
}

nums = [5, 10]
roman = ['V', 'X']


def arabic_to_roman_up_to_13(arabic):
    num = arabic
    result = ''
    if num in mapping.keys():
        return mapping[num]
    if num < 5:
        while num > 0:
            result += 'I'
            num -= 1
        return result
    elif num < 10:
        result = 'V'
        num = arabic - 5
        while num > 0:
            result += 'I'
            num -= 1
        return result
    else:
        result = 'X'
        num = arabic - 10
        while num > 0:
            result += 'I'
            num -= 1
        return result


def arabic_to_roman(arabic):
    num = arabic
    if num in mapping.keys():
        return mapping[num]
    index = 0
    result = ''
    while index < len(nums):
        if num < nums[index]:
            if index >= 1:
                num = arabic - nums[index - 1]
                result += roman[index - 1]
            while num > 0:
                result += 'I'
                num -= 1
            return result
        else:
            index = index + 1
