# Number Length
# https://py.checkio.org/mission/number-length/share/a5fdf5167393105c0534e6f8b10ab6d5/
# By Evans Hua @ 20220313

def number_length(a: int) -> int:
    # your code here
    l = len (str(a))
    return l


if __name__ == '__main__':
    print("Example:")
    print(number_length(10))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert number_length(10) == 2
    assert number_length(0) == 1
    assert number_length(4) == 1
    assert number_length(44) == 2
    print("Coding complete? Click 'Check' to earn cool rewards!")
