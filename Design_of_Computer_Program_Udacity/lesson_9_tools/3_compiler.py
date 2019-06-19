"""
  User: Liujianhan
  Time: 21:33
 """
__author__ = 'liujianhan'


def match(pattern, text):
    """Match pattern against start of text; return longest match found or None."""
    remainders = pattern(text)
    if remainders:
        shortest = min(remainders, key=len)
        return text[:len(text) - len(shortest)]


def lit(s): return lambda text: {text[len(s):]} if text.startswith(s) else null


def seq(x, y): return lambda text: set().union(*map(y, x(text)))


def alt(x, y): return lambda text: x(text) | y(text)


def oneof(chars): return lambda t: {t[1:]} if t and t[0] in chars else null


def star(x): return lambda t: {t} | {t2 for t1 in x(t) if t1 != t for t2 in star(x)(t1)}


dot = lambda t: {t[1:]} if t else null

eol = lambda t: {''} if t == '' else null

null = frozenset([])


def test():
    g = alt(lit('a'), lit('b'))
    assert g('abc') == {'bc'}
    return 'test passes'


if __name__ == '__main__':
    print(test())
