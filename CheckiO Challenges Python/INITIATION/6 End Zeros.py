# End Zeros
# https://py.checkio.org/mission/end-zeros/share/82d79bf9147e1a4c56beb3dafdbfe7a3/
# By Evans Hua @ 20220403

def end_zeros(num: int) -> int:
    # your code here
    s = str(num)
    end_zeros = len(s) - len(s.rstrip('0'))
    return end_zeros


if __name__ == '__main__':
    print("Example:")
    print(end_zeros(0))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert end_zeros(0) == 1
    assert end_zeros(1) == 0
    assert end_zeros(10) == 1
    assert end_zeros(101) == 0
    assert end_zeros(245) == 0
    assert end_zeros(100100) == 2
    print("Coding complete? Click 'Check' to earn cool rewards!")
