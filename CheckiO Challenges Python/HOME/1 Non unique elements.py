# Non unique elements
# CheckiO: https://py.checkio.org/mission/non-unique-elements/share/9b6de30be9feba571d23cc454b7aa247/
# By Evans Hua @ 20221002
#Your optional code here
#You can import some modules or create additional functions

def checkio(data: list) -> list:
    #Your code here
    #It's main function. Don't remove this function
    #It's used for auto-testing and must return a result for check.  

    #replace this for solution
    from collections import Counter
    unique = [item for item, count in Counter(data).items() if count == 1]
    non_unique = [item for item in data if (item not in unique)]
    return non_unique

#Some hints
#You can use list.count(element) method for counting.
#Create new list with non-unique elements
#Loop over original list

if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert list(checkio([1, 2, 3, 1, 3])) == [1, 3, 1, 3], "1st example"
    assert list(checkio([1, 2, 3, 4, 5])) == [], "2nd example"
    assert list(checkio([5, 5, 5, 5, 5])) == [5, 5, 5, 5, 5], "3rd example"
    assert list(checkio([10, 9, 10, 10, 9, 8])) == [10, 9, 10, 10, 9], "4th example"
    print("It is all good. Let's check it now")
