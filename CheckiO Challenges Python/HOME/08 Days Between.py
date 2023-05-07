# Days Between
# CheckiO:https://py.checkio.org/mission/days-diff/share/04f5391af9e2e53a180759136826fd8a/
# By Evans Hua @ 20230507
def days_diff(a, b):
    # your code here
    import datetime
    adt = datetime.datetime(*a)
    bdt = datetime.datetime(*b)
    res = abs((adt-bdt).days)
    return res

if __name__ == "__main__":
    print("Example:")
    print(days_diff((1982, 4, 19), (1982, 4, 22)))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert days_diff((1982, 4, 19), (1982, 4, 22)) == 3
    assert days_diff((2014, 1, 1), (2014, 8, 27)) == 238
    assert days_diff((2014, 8, 27), (2014, 1, 1)) == 238
    print("Coding complete? Click 'Check' to earn cool rewards!")
