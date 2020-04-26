#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import pprint
pp = pprint.PrettyPrinter(indent=4)

parser = argparse.ArgumentParser(description="コマンドライン引数取得のテストプログラム")
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='足し算スクリプト')

parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers')

args = parser.parse_args()
print(args.accumulate(args.integers))

"""
##:情報源

* https://docs.python.jp/3/library/argparse.html
"""

