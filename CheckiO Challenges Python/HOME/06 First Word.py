# First Word
# CheckiO:https://py.checkio.org/mission/first-word/share/220635d75f94eb57d8bfdea4e10762bc/
# By Evans Hua @ 20230212
def first_word(text: str) -> str:
    """
    returns the first word in a given text.
    """
    # your code here
    import re
    t = re.sub(r'[,.]',' ', text)
    t = t.split()
    return t[0]

if __name__ == "__main__":
    print("Example:")
    print(first_word("Hello world"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert first_word("Hello world") == "Hello"
    assert first_word(" a word ") == "a"
    assert first_word("don't touch it") == "don't"
    assert first_word("greetings, friends") == "greetings"
    assert first_word("... and so on ...") == "and"
    assert first_word("hi") == "hi"
    assert first_word("Hello.World") == "Hello"
    print("Coding complete? Click 'Check' to earn cool rewards!")
