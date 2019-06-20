"""
  User: Liujianhan
  Time: 17:25
 """
__author__ = 'liujianhan'


def grammar_(description):
    """Convert a description to  a grammar."""
    G = {}
    for line in description.split('\n'):
        if line != '':
            lhs, rhs = line.split('    => ')
            alternatives = rhs.split(' | ')
            G[lhs] = tuple(map(str.split, alternatives))
    return G


def grammar(description, whitespace=r'\s*'):
    """Convert a description to  a grammar.
    Deal with whitespaces."""
    G = {' ': whitespace}
    description = description.replace('\t', ' ')    # no tabs
    for line in split(description, '\n'):
        lhs, rhs = split(line, '    => ', 1)
        alternatives = split(rhs, ' | ')
        G[lhs] = tuple(map(split, alternatives))
    return G


def split(text, sep=None, max_split=-1):
    """Like str.split applied to text, but strips whitespace from each piece."""
    return [t.strip() for t in text.strip().split(sep, max_split) if t]


tmp = r"""
exp    => term [+-] exp | term
term    => factor [*/] term | factor
factor    => fun_call | var | num | [(] exp [)]
fun_call    => var [(] exps [)]
exps    => exp [,] exps | exp
var    => [a-zA-Z]\w*
num    => [-+]?[0-9]+([.][0-9]*)?
"""

G = grammar(tmp)

if __name__ == '__main__':
    print(G)
