#!/usr/bin/env python
# -*- coding:utf-8 -*-

def fact_max(n):
    return fact_iter(n,1)

def fact_iter(n,total):
    if n==1:
        return total
    return fact_iter(n-1,n*total)

print fact_max(5)

