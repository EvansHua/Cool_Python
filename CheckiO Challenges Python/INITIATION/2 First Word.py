# First Word
# https://py.checkio.org/mission/first-word-simplified/share/0396465f40bce1f7b61e1db7d8dc3f0b/
# By Evans Hua @ 20220313

def first_word(text: str) -> str:
    """
    returns the first word in a given text.
    """
    # your code here
    all_words = text.split()
    first = all_words [0]
    #return text[0:2]
    return first

if __name__ == "__main__":
    print("Example:")
    print(first_word("Hello world"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert first_word("Hello world") == "Hello"
    assert first_word("a word") == "a"
    assert first_word("hi") == "hi"
    print("Coding complete? Click 'Check' to earn cool rewards!")
