# Acceptable Password I
# https://py.checkio.org/mission/acceptable-password-i/share/b10e50a8808c1f282bbcdd3a40dcef85/
# By Evans Hua @ 20220313

def is_acceptable_password(password: str) -> bool:
    # your code here
    length = len(password)
    if length > 6:
        result = True
    else:
        result = False
    return result

if __name__ == '__main__':
    print("Example:")
    print(is_acceptable_password('short'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_acceptable_password('short') == False
    assert is_acceptable_password('muchlonger') == True
    assert is_acceptable_password('ashort') == False
    print("Coding complete? Click 'Check' to earn cool rewards!")
