#!/usr/bin/env python
# -*- coding: utf-8 -*-

import fractions
def reduce(p, q):
    common = fractions.gcd(p, q)
    return (p // common, q // common)

if __name__ == '__main__':

   # 154/238の約分し既約分数にする
   result = reduce(154, 238)
   print(result)

   # 105/455の約分し既約分数にする
   result = reduce(105, 455)
   print(result)

