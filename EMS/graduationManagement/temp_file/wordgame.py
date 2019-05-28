#!/usr/bin/env python
# coding: utf-8

# # WordGame
# 
# https://github.com/smarr/CLIPS/blob/master/examples/wordgame.clp

# In[1]:


from functools import partial, reduce
from itertools import takewhile
import operator as op

from pyknow import *


class Number(Fact):
    pass


class Letter(Fact):
    pass


class Combination(Fact):
    pass

until_none = partial(takewhile, lambda x: x is not None)


def check_combination(d=None, t=None, l=None, r=None, a=None,
                      e=None, n=None, b=None, o=None, g=None):
    """Check a partial solution."""

    left_1 = list(until_none(reversed([g, e, r, a, l, d])))
    left_2 = list(until_none(reversed([d, o, n, a, l, d])))
    right = list(until_none(reversed([r, o, b, e, r, t])))

    a = sum((l[0] * 10 ** e) + (l[1] * 10 ** e)
            for e, l in enumerate(zip(left_1, left_2)))
    b = sum((l * 10 ** e) for e, l in enumerate(right))

    if len(left_1) < 6:
        a = a % 10**len(right)

    return a == b


def C(name, neq=""):
    """
    Ex: name="c", neq="tar" => W("c") & ~W("t") & ~W("a") & ~W("r")

    """
    if neq:
        return W(name) & reduce(op.and_, [~W(c) for c in neq])
    else:
        return W(name)


class WordGame(KnowledgeEngine):
    @Rule()
    def startup(self):
        print("The problem is")
        print("    GERALD")
        print("  + DONALD")
        print("    ------")
        print("  = ROBERT")
        print()

        for n in range(10):
            self.declare(Number(n))

        for l in set("GERALD" + "DONALD" + "ROBERT"):
            self.declare(Letter(l))

    @Rule(Number(MATCH.n),
          Letter(MATCH.l))
    def generate_combinations(self, n, l):
        self.declare(Combination(l, n))

    @Rule(Combination("D", C("d")),
          Combination("T", C("t", neq="d")),
          TEST(check_combination),
          Combination("L", C("l", neq="dt")),
          Combination("R", C("r", neq="dtl")),
          TEST(check_combination),
          Combination("A", C("a", neq="dtlr")),
          Combination("E", C("e", neq="dtlra")),
          TEST(check_combination),
          Combination("N", C("n", neq="dtlrae")),
          Combination("B", C("b", neq="dtlraen")),
          TEST(check_combination),
          Combination("O", C("o", neq="dtlraenb")),
          Combination("G", C("g", neq="dtlraenbo")),
          TEST(check_combination))
    def find_solution(self, g, e, r, a, l, d, o, n, b, t):
        print("A solution is:")
        print("  G =", g)
        print("  E =", e)
        print("  R =", r)
        print("  A =", a)
        print("  L =", l)
        print("  D =", d)
        print("  O =", o)
        print("  N =", n)
        print("  B =", b)
        print("  T =", t)
        print()
        print("    ", g, e, r, a, l, d)
        print("  + ", d, o, n, a, l, d)
        print("    ", "------")
        print("  = ", r, o, b, e, r, t)
        print()


# In[2]:


wg = WordGame()
wg.reset()
wg.run()

