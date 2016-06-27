#!/usr/bin/env python
# -*-coding:utf-8-*-

def power(x,n=2):
    s=x
    while n>1:
        n=n-1
        s=s*x
    return s

print'power(5)=%s'%power(5)
