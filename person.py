#!/usr/bin/env python
# -*- coding:utf-8 -*-

def person(name, age, **kw):
    print 'name:',name, 'age:',age, 'other:',kw

person('Jacey',27)

person('Bob',35,city='Beijing')

person('Adam',45,gender='M',job='Engineer')

kw={'city':'Beijing','job':'Engineer'}
person('Jack',24,city=kw['city'],job=kw['job'])

kw={'city':'Shanghai','job':'Engineer'}
person('Jack',24,**kw)
