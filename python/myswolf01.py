#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__='Swolf'

import sys

def test():
    args = sys.argv
    if len(args)==1:
        print('1Hello %s!' % args[0])
    elif len(args)==2:
        print('2Hello %s' % args[1])
    else:
        print('3Too many arguments!')

if __name__=='__main__':
    test()
