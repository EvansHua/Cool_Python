# Three Words
# CheckiO: https://py.checkio.org/mission/three-words/share/dd2252765d9f75b116ba2401c69cbee8/
# By Evans Hua @ 20230430

def checkio(words: str) -> bool:
    from itertools import groupby
    lst = words.split()
    lst1 = [(i,'/') [i.isdigit()] for i in lst]
    chunks = (list(g) for k,g in groupby(lst1, key=lambda x: x != '/') if k)
    r = False
    for chunk in chunks:
        if len(chunk) >= 3:
            r = True
    return r

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print('Example:')
    print(checkio("Hello World hello"))
    
    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
