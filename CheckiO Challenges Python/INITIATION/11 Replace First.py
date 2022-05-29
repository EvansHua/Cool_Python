# Replace First
# https://py.checkio.org/mission/replace-first/share/737426b18fdd04bd0e89f761334c7a23/
# By Evans Hua @ 20220529

from typing import Iterable

def replace_first(items: list) -> Iterable:
    # your code here
    if items != []:
        first = items[0]
        items.append (first)
        items.pop(0)
    return items

if __name__ == "__main__":
    print("Example:")
    print(list(replace_first([1, 2, 3, 4])))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(replace_first([1, 2, 3, 4])) == [2, 3, 4, 1]
    assert list(replace_first([1])) == [1]
    assert list(replace_first([])) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")
