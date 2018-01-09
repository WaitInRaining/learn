#!usr/bin/python
#coding:utf-8
import math
import sec

def intersect(seq1, seq2):
    res =[]
    for x in seq1:
        if x in seq2:
            res.append(x)
    return res;
s1 = [1,2,3,4,5]
s2 = (1,2,3,4,5)
print  intersect(s1, s2)
print sec.a
def marker():
    N = 2
    def action(M):
        return M**N
    return action

f = marker()
print f(3)
def func():
    x = 3
    action = (lambda n:x ** n)
    return action

x = func()
print x(2)
def makeActions():
    acts =[]
    for i in range(5):
        acts.append(lambda x, i=i: i ** x)
    return acts
x = makeActions()
print x[0](4)
print range(5)

q = 'hahah'
def fun():
    global  q
    q = 'heihei'
fun()
print q

e = [1,2,3]
def fun(c,d):
    d = d[:]
    c = 3
    d[0] ='heihei'
f = 2;
fun(f,e)
print f,e
