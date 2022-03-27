# The Most Frequent
# https://py.checkio.org/mission/the-most-frequent/share/741d414a8dd4107d3cd1e0cf78a4b7b8/
# By Evans Hua @ 20220327

from statistics import mode
def most_frequent(data: list) -> str:
    """
    determines the most frequently occurring string in the sequence.
    """
    # your code here 
    return mode(data)


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    print("Example:")
    print(most_frequent(["a", "b", "c", "a", "b", "a"]))

    assert most_frequent(["a", "b", "c", "a", "b", "a"]) == "a"

    assert most_frequent(["a", "a", "bi", "bi", "bi"]) == "bi"
    print("Done")
