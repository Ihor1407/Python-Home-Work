import re


def is_palindrome(text):
    low_text = text.lower()
    clear_text = re.sub('[^a-z0-9]', '', low_text)
    return clear_text == clear_text[::-1]


assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")
