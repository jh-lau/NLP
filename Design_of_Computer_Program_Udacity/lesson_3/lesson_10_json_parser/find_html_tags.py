"""
  User: Liujianhan
  Time: 23:01
 """
__author__ = 'liujianhan'
import re


def find_tags(text):
    parms = '(\w+\s*=\s*"[^"]*"\s*)*'
    tags = '(<\s*\w+\s*' + parms + '\s*/?>)'
    pattern = r'<\s*[a,b].*?>'
    # return re.findall(pattern, text)
    return re.findall(tags, text)


test_text1 = """
My favorite website in the world is probably 
<a href="www.udacity.com">Udacity</a>. If you want 
that link to open in a <b>new tab</b> by default, you should
write <a href="www.udacity.com"target="_blank">Udacity</a>
instead!
"""

test_text2 = """
Okay, so you passed the first test case. <let's see> how you 
handle this one. Did you know that 2 < 3 should return True? 
So should 3 > 2. But 2 > 3 is always False.
"""

test_text3 = """
It's not common, but we can put a LOT of whitespace into 
our HTML tags. For example, we can make something bold by
doing <         b           > this <   /b    >, Though I 
don't know why you would ever want to.
"""


def test():
    assert find_tags(test_text1) == ['<a href="www.udacity.com">',
                                     '<b>',
                                     '<a href="www.udacity.com"target="_blank">']
    assert find_tags(test_text2) == []
    assert find_tags(test_text3) == ['<         b           >']
    return 'tests pass'


if __name__ == '__main__':
    print(test())
