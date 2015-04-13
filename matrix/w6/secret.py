#!/usr/bin/env python
#-*- coding:utf-8 -*-

import random
from GF2 import one
from vecutil import list2vec
from independence import is_independent

def randGF2(): return random.randint(0,1)*one

a0 = list2vec([one, one,   0, one,   0, one])
b0 = list2vec([one, one,   0,   0,   0, one])

def choose_secret_vector(s,t):
    while True:
        u = list2vec([randGF2() for idx in range(6)])
        if (a0*u == s) and (b0*u == t):
            return u

def problem1():
    print()
    u = choose_secret_vector(one,0)
    print(u)
    print(a0*u)
    print(b0*u)
    print('~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~')
    u = choose_secret_vector(0,one)
    print(u)
    print(a0*u)
    print(b0*u)
    print('~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~')
    u = choose_secret_vector(one,one)
    print(u)
    print(a0*u)
    print(b0*u)
    print('~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~')
    u = choose_secret_vector(0,0)
    print(u)
    print(a0*u)
    print(b0*u)
    print()

# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

def randomvector():
    return list2vec([randGF2() for idx in range(6)])

def problem2():
    cont = 0
    while True:
        a1 = randomvector()
        b1 = randomvector()
        a2 = randomvector()
        b2 = randomvector()
        a3 = randomvector()
        b3 = randomvector()
        a4 = randomvector()
        b4 = randomvector()
        #lista = [a0,b0,a1,b1,a2,b2,a3,b3,a4,b4]
        #lista = [a0,b0,a1,b1,a2,b2]
        cond1 = is_independent([a1,b1,a2,b2,a3,b3])
        cond2 = is_independent([a1,b1,a2,b2,a4,b4])
        cond3 = is_independent([a1,b1,a3,b3,a4,b4])
        cond4 = is_independent([a2,b2,a3,b3,a4,b4])
        cond10 = is_independent([a0,b0,a1,b1,a2,b2])
        cond20 = is_independent([a0,b0,a1,b1,a3,b3])
        cond30 = is_independent([a0,b0,a1,b1,a4,b4])
        cond40 = is_independent([a0,b0,a2,b2,a3,b3])
        cond50 = is_independent([a0,b0,a2,b2,a4,b4])
        cond60 = is_independent([a0,b0,a3,b3,a4,b4])
        cont += 1
        if cont % 50000 == 0:
            print(cont)
        if cond1 and cond2 and cond3 and cond4 and cond10 and cond20 and cond30 and cond40 and cond50 and cond60:
            break
    print('secret_a0 = Vec({}, {})'.format(a0.D, a0.f))
    print('secret_b0 = Vec({}, {})'.format(b0.D, b0.f))
    print('secret_a1 = Vec({}, {})'.format(a1.D, a1.f))
    print('secret_b1 = Vec({}, {})'.format(b1.D, b1.f))
    print('secret_a2 = Vec({}, {})'.format(a2.D, a2.f))
    print('secret_b2 = Vec({}, {})'.format(b2.D, b2.f))
    print('secret_a3 = Vec({}, {})'.format(a3.D, a3.f))
    print('secret_b3 = Vec({}, {})'.format(b3.D, b3.f))
    print('secret_a4 = Vec({}, {})'.format(a4.D, a4.f))
    print('secret_b4 = Vec({}, {})'.format(b4.D, b4.f))
    

# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

def main():
    problem2()
    

# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

if __name__ == '__main__':
    main()


