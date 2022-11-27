# Sum Numbers
# CheckiO: https://py.checkio.org/mission/sum-numbers/share/30a756ab4ecf5ed7a4d7321fe172c7a0/
# By Evans Hua @ 20221127
def sum_numbers(text: str) -> int:
    # your code here
    lst = text.split()
    r = [s for s in lst if s.isdigit()]
    r = [int(i) for i in r]
    return sum(r)
  
if __name__ == "__main__":
    print("Example:")
    print(sum_numbers("hi"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert sum_numbers("hi") == 0
    assert sum_numbers("who is 1st here") == 0
    assert sum_numbers("my numbers is 2") == 2
    assert (
        sum_numbers(
            "This picture is an oil on canvas "
            "painting by Danish artist Anna "
            "Petersen between 1845 and 1910 year"
        )
        == 3755
    )
    assert sum_numbers("5 plus 6 is") == 11
    assert sum_numbers("") == 0
    print("Coding complete? Click 'Check' to earn cool rewards!")
