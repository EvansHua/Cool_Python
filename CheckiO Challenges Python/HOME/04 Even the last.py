# Even the last
# CheckiO: https://py.checkio.org/mission/even-last/share/4c9f9c1afc1eddf2c8de9a82de732ac5/
# By Evans Hua @ 20230108

def checkio(array):
    """
        sums even-indexes elements and multiply at the last
    """
    if len(array) == 0:
        r = 0
    else:
        r = sum(array[0::2]) * array[-1]
    return r

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
    assert checkio([1, 3, 5]) == 30, "(1+5)*5=30"
    assert checkio([6]) == 36, "(6)*6=36"
    assert checkio([]) == 0, "Empty"
