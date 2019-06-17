"""
  User: Liujianhan
  Time: 16:22
 """
__author__ = 'liujianhan'


def is_palindrome(string):
    return string == string[::-1]


def index_(string, sub_string):
    start_index = string.find(sub_string)
    end_index = start_index + len(sub_string)
    return start_index, end_index


def longest_sub_palindrome_slice(text, fill='*'):
    """Return (i, j) such that text[i:j] is the longest palindrome in text."""
    if len(text) == 0:
        return 0, 0
    result = ''
    text_new = fill.join(list(text)).upper()
    for index, _ in enumerate(text_new):
        for i in range(len(text_new)):
            start = index - i
            end = index + i + 1
            if start >= 0 and end > 0 and start is not end:
                string = text_new[start:end].strip(fill)
                if is_palindrome(string):
                    if len(result) < len(string):
                        result = string
                else:
                    break
            elif start < 0:
                break
            else:
                continue
    result = ''.join(result.split(fill))
    result = index_(text.upper(), result)
    return result


def test():
    L = longest_sub_palindrome_slice
    assert L('racecar') == (0, 7)
    assert L('Racecar') == (0, 7)
    assert L('RacecarX') == (0, 7)
    assert L('Race carr') == (7, 9)
    assert L('') == (0, 0)
    assert L('something rac e car going') == (8, 21)
    assert L('xxxxx') == (0, 5)
    assert L('Mad am I ma dam.') == (0, 15)
    return 'tests pass'


if __name__ == '__main__':
    test()
