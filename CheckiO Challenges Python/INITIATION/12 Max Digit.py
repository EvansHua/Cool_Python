# Max Digit
# https://py.checkio.org/mission/max-digit/share/46ebeda34e4a2a96e33f04380e9f39c6/
# By Evans Hua @ 20220612

def max_digit(number: int) -> int:
    # your code here
    r = list (map(int, str(number)))
    return max(r)

if __name__ == '__main__':
    print("Example:")
    print(max_digit(0))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert max_digit(0) == 0
    assert max_digit(52) == 5
    assert max_digit(634) == 6
    assert max_digit(1) == 1
    assert max_digit(10000) == 1
    print("Coding complete? Click 'Check' to earn cool rewards!")
