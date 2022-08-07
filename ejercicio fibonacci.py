# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 20:20:55 2022

@author: fernando.rivera
"""
def fib(n):
    a, b = 0,1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()
fib(10)