# Backward String
# https://py.checkio.org/mission/backward-string/share/7d8e12e5ed03d09114ca9e518daef61e/
# By Evans Hua @ 20220403

def backward_string(val: str) -> str:
    # your code here
    txt = val [::-1]
    return txt


if __name__ == '__main__':
    print("Example:")
    print(backward_string('val'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert backward_string('val') == 'lav'
    assert backward_string('') == ''
    assert backward_string('ohho') == 'ohho'
    assert backward_string('123456789') == '987654321'
    print("Coding complete? Click 'Check' to earn cool rewards!")
