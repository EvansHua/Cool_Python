# Remove All Before
# https://py.checkio.org/mission/remove-all-before/share/7bc0f42e11a097a0e1a2ee065bb98039/
# By Evans Hua @ 20220417
from typing import Iterable

def remove_all_before(items: list, border: int) -> Iterable:
    # your code here
    start_i = 0
    for ind, value in enumerate(items):
        if value == border:
            start_i = ind
            break
    end_i = len (items)
    i = range (start_i, end_i)
    element = []
    for index in i:
        element.append(items[index])
    return element

if __name__ == '__main__':
    print("Example:")
    print(list(remove_all_before([1, 2, 3, 4, 5], 3)))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(remove_all_before([1, 2, 3, 4, 5], 3)) == [3, 4, 5]
    assert list(remove_all_before([1, 1, 2, 2, 3, 3], 2)) == [2, 2, 3, 3]
    assert list(remove_all_before([1, 1, 2, 4, 2, 3, 4], 2)) == [2, 4, 2, 3, 4]
    assert list(remove_all_before([1, 1, 5, 6, 7], 2)) == [1, 1, 5, 6, 7]
    assert list(remove_all_before([], 0)) == []
    assert list(remove_all_before([7, 7, 7, 7, 7, 7, 7, 7, 7], 7)) == [7, 7, 7, 7, 7, 7, 7, 7, 7]
    print("Coding complete? Click 'Check' to earn cool rewards!")
