# Is Even
# https://py.checkio.org/mission/is-even/share/1a0e59e4a9e7406aa508298b4ae880dc/
# By Evans Hua @ 20220918

def is_even(num: int) -> bool:
    # your code here
    return num % 2 == 0

if __name__ == '__main__':
    print("Example:")
    print(is_even(2))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_even(2) == True
    assert is_even(5) == False
    assert is_even(0) == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
