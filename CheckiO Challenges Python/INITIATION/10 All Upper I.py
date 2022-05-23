# All Upper I
# https://py.checkio.org/mission/all-upper/share/fce072349eb31ef0f0bce70703070cb2/
# By Evans Hua @ 20220523

def is_all_upper(text: str) -> bool:
    # your code here
    text1 = text.replace (' ', '')
    if text1.isalpha():
        r = text1.isupper()
    else:
        r = True
    return r

if __name__ == '__main__':
    print("Example:")
    print(is_all_upper('ALL UPPER'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_all_upper('ALL UPPER') == True
    assert is_all_upper('all lower') == False
    assert is_all_upper('mixed UPPER and lower') == False
    assert is_all_upper('') == True
    assert is_all_upper('     ') == True
    assert is_all_upper('444') == True
    assert is_all_upper('55 55 5') == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
