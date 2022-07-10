# Split Pairs
# https://py.checkio.org/mission/split-pairs/share/f3d66fb9ad9f14663655adbce4cf15b2/
# By Evans Hua @ 20220710

def split_pairs(a):
    # your code here
    if a != '':  # non blank string
        if len(a) % 2 != 0:
            a += '_'
        m = 2
        c = [a[i:i+m] for i in range(0,len(a), m)]
    else:  # blank string
        c = []
    return c

if __name__ == '__main__':
    print("Example:")
    print(list(split_pairs('abcd')))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(split_pairs('abcd')) == ['ab', 'cd']
    assert list(split_pairs('abc')) == ['ab', 'c_']
    assert list(split_pairs('abcdf')) == ['ab', 'cd', 'f_']
    assert list(split_pairs('a')) == ['a_']
    assert list(split_pairs('')) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")
