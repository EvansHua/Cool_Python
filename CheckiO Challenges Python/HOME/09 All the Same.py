# All the Same
# CheckiO:https://py.checkio.org/mission/all-the-same/share/01be0fad95e8a6e32c732a8ae824564a/
# By Evans Hua @ 20230716

from typing import List, Any

def all_the_same(elements: List[Any]) -> bool:
    # your code here
    check = True
    if elements == []:
        check == True
    else:
        ele = elements [0]
        for item in elements:
            if ele != item:
                check = False
                break;
    return check

print("Example:")
print(all_the_same([1, 1, 1]))

assert all_the_same([1, 1, 1]) == True
assert all_the_same([1, 2, 1]) == False
assert all_the_same([1, 1, 1, 2]) == False
assert all_the_same([2, 1, 1, 1]) == False
assert all_the_same([]) == True
assert all_the_same([1]) == True

print("The mission is done! Click 'Check Solution' to earn rewards!")
