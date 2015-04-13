#!/usr/bin/env python
#-*- coding:utf-8 -*-

from cancer_data import read_training_data
from machine_learning_lab import *

def problem1():
    print(signum(Vec({1,2,3},{1:2, 2:-1})) == Vec({1,2,3},{1:1,2:-1,3:1}))

def problem2():
    A = Mat(({'a','b','c'},{'A','B'}), {('a','A'):-4, ('a','B'):3, ('b','A'):1, ('b','B'):8, ('c','A'):5, ('c','B'):2})
    b = Vec({'a','b','c'}, {'a':1, 'b':-1,'c':1})
    w = Vec({'A','B'}, {'A':1, 'B':-2})
    print(fraction_wrong(A, b, w))

# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

def problem3():
    A = Mat(({'a','b','c'},{'A','B'}), {('a','A'):-4, ('a','B'):3, ('b','A'):1, ('b','B'):8, ('c','A'):5, ('c','B'):2})
    b = Vec({'a','b','c'}, {'a':1, 'b':-1,'c':1})
    w = Vec({'A','B'}, {'A':1, 'B':-2})
    print(loss(A, b, w))

# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

def problem4():
    A = Mat(({'a','b','c'},{'A','B'}), {('a','A'):-4, ('a','B'):3, ('b','A'):1, ('b','B'):8, ('c','A'):5, ('c','B'):2})
    b = Vec({'a','b','c'}, {'a':1, 'b':-1,'c':1})
    w = Vec({'A','B'}, {'A':1, 'B':-2})
    print(find_grad(A, b, w) == Vec({'B', 'A'},{'B': -290, 'A': 60}))

# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

def problem5():
    A = Mat(({'a','b','c'},{'A','B'}), {('a','A'):-4, ('a','B'):3, ('b','A'):1, ('b','B'):8, ('c','A'):5, ('c','B'):2})
    b = Vec({'a','b','c'}, {'a':1, 'b':-1,'c':1})
    w = Vec({'A','B'}, {'A':1, 'B':-2})
    sigma = .1
    print(gradient_descent_step(A, b, w, sigma) == Vec({'B', 'A'},{'B': 27.0, 'A': -5.0}))

# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

def extra():
    A = Mat(({'a','b','c'},{'A','B'}), {('a','A'):-4, ('a','B'):3, ('b','A'):1, ('b','B'):8, ('c','A'):5, ('c','B'):2})
    b = Vec({'a','b','c'}, {'a':1, 'b':-1,'c':1})
    w = Vec({'A','B'}, {'A':1, 'B':-2})
    sigma = .1
    gradient_descent(A, b, w, sigma, 4)

# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

def main():
    extra()
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

if __name__ == '__main__':
    main()


