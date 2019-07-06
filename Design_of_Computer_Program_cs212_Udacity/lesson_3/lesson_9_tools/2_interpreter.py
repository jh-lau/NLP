"""
  User: Liujianhan
  Time: 14:24
 """
__author__ = 'liujianhan'

null = frozenset()


def lit(string): return 'lit', string


def seq(x, y): return 'seq', x, y


def alt(x, y): return 'alt', x, y


def star(x): return 'star', x


def plus(x): return seq(x, star(x))


def opt(x): return alt(lit(''), x)


def oneof(chars): return 'oneof', tuple(chars)


dot = ('dot',)
eol = ('eol',)


def components(pattern):
    """Return the op, x and y arguments; x and y are None if missing."""
    x = pattern[1] if len(pattern) > 1 else None
    y = pattern[2] if len(pattern) > 2 else None
    return pattern[0], x, y


def search(pattern, text):
    """Match pattern anywhere in text; return longest earliest match or None."""
    for i in range(len(text)):
        m = match(pattern, text[i:])
        if m is not None:
            return m


def match(pattern, text):
    """Match pattern against start of text; return longest match found or None."""
    remainders = matchset(pattern, text)
    if remainders:
        shortest = min(remainders, key=len)
        return text[:len(text)-len(shortest)]


def matchset(pattern, text):
    """Match pattern at start of text; return a set of remainders of text.
    For example, if matchset were called with the pattern star(lit(a)) and
    the text 'aaab', matchset would return a set with elements
    {'aaab', 'aab', 'ab', 'b'}, since a* can consume one, two
    or all three of the a's in the text."""
    op, x, y = components(pattern)
    if 'lit' == op:
        return {text[len(x):]} if text.startswith(x) else null
    elif 'seq' == op:
        return set(t2 for t1 in matchset(x, text) for t2 in matchset(y, t1))
    elif 'alt' == op:
        return matchset(x, text) | matchset(y, text)
    elif 'dot' == op:
        return {text[1:]} if text else null
    elif 'oneof' == op:
        return {text[1:]} if any(text.startswith(c) for c in x) else null
    elif 'eol' == op:
        return {''} if text == '' else null
    elif 'star' == op:
        return {text} | set(t2 for t1 in matchset(x, text)
                            for t2 in matchset(pattern, t1) if t1 != text)
    else:
        raise ValueError(f"unknown pattern: {pattern}")


def test():
    assert lit('abc') == ('lit', 'abc')
    assert seq(('lit', 'a'), ('lit', 'b')) == ('seq', ('lit', 'a'), ('lit', 'b'))
    assert alt(('lit', 'a'), ('lit', 'b')) == ('alt', ('lit', 'a'), ('lit', 'b'))
    assert star(('lit', 'a')) == ('star', ('lit', 'a'))
    assert plus(('lit', 'c')) == ('seq', ('lit', 'c'), ('star', ('lit', 'c')))
    assert opt(('lit', 'x')) == ('alt', ('lit', ''), ('lit', 'x'))
    assert oneof('abc') == ('oneof', ('a', 'b', 'c'))

    assert match(('star', ('lit', 'a')), 'aaabcd') == 'aaa'
    assert match(('alt', ('lit', 'b'), ('lit', 'c')), 'ab') is None
    assert match(('alt', ('lit', 'b'), ('lit', 'a')), 'ab') == 'a'
    assert search(('alt', ('lit', 'b'), ('lit', 'c')), 'ab') == 'b'
    return 'tests pass'


if __name__ == '__main__':
    print(test())
