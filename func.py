#!/usr/bin/env python
# -*-coding:utf-8-*-

def func(a,b,c=0,*args,**kw):
    print 'a:',a
    print 'b:',b
    print 'c:',c
    print 'args=',args
    print 'kw=',kw
    print '------这是一条开心的分割线--------'

func(1,2)

func(1,2,c=3)

func(1,2,3,'a','b','c')

func(1,2,3,'a','b',x=99)

args=(1,2,3,4)
kw={'x':99}
func(*args,**kw)
