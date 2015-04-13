#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os
from vec import Vec
from GF2 import one
from mat import Mat
from matutil import mat2rowdict

def is_echelon(A):
    '''
    Input:
        - A: a list of row lists
    Output:
        - True if A is in echelon form
        - False otherwise
    '''
    prev = -1 if A[0][0] != 0 else 0
    for row in A:
        for idx, col in enumerate(row):
            if col != 0:
                if prev >= idx:
                    return False
                prev = idx
                break
        else:
            prev = len(row) - 1
    return True

def problem1():
    print(is_echelon([[9,-1,2],[0,4,5],[0,0,2]]))
    print(is_echelon([[0,4,5],[0,3,0],[0,0,2]]))
    print(is_echelon([[9,10]]))
    print(is_echelon([[5]]))
    print(is_echelon([[1],[1]]))
    print(is_echelon([[0]]))
    print(is_echelon([[0],[1]]))
    print('~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~')
    print(is_echelon([[2,1,0],[0,-4,0],[0,0,1]]))
    print(is_echelon([[2,1,0],[-4,0,0],[0,0,1]]))
    print(is_echelon([[2,1,0],[0,3,0],[1,0,1]]))
    print(is_echelon([[1,1,1,1,1],[0,2,0,1,3],[0,0,0,5,3]]))
    print('~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~')
    print(is_echelon([[1,1,1],[0,1,0],[0,0,0],[0,0,0]]))
    print(is_echelon([[1,1,1],[0,0,0],[0,0,1]]))

# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

def echelon_solve(row_list, label_list, b):
    '''
    Input:
        - row_list: a list of Vecs
        - label_list: a list of labels establishing an order on the domain of
                      Vecs in row_list
        - b: a vector (represented as a list)
    Output:
        - Vec x such that row_list * x is b
    >>> D = {'A','B','C','D','E'}
    >>> U_rows = [Vec(D, {'A':one, 'E':one}), Vec(D, {'B':one, 'E':one}), Vec(D,{'C':one})]
    >>> b_list = [one,0,one]
    >>> cols = ['A', 'B', 'C', 'D', 'E']
    >>> echelon_solve(U_rows, cols, b_list) == Vec({'B', 'C', 'A', 'D', 'E'},{'B': 0, 'C': one, 'A': one})
    True
    '''
    x = Vec(set(label_list), {})
    for row, bval in reversed(zip(row_list, b)):
        # find left-most nonzero
        who = None
        for col in label_list:
            if row[col] != 0:
                who = col
                break
        # row != all-zero row
        if who:
            x[who] = (bval - row * x) / row[who]
    return x

def problem5():
    D = {'A','B','C','D','E'}
    U_rows = [Vec(D, {'A':one, 'E':one}), Vec(D, {'B':one, 'E':one}), Vec(D,{'C':one})]
    b_list = [one,0,one]
    cols = ['A', 'B', 'C', 'D', 'E']
    print(echelon_solve(U_rows, cols, b_list) == Vec({'B', 'C', 'A', 'D', 'E'},{'B': 0, 'C': one, 'A': one}))

# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

def problem7():
    A = Mat(({'a','b','c','d'},{'A','B','C','D'}), {('a','A'):one, ('a','B'):one, ('a','D'):one, ('b','A'):one, ('b','D'):one, ('c','A'):one, ('c','B'):one, ('c','C'):one, ('c','D'):one, ('d','C'):one, ('d','D'):one})
    M = Mat(({0,1,2,3},{'a','b','c','d'}), {(0,'a'):one, (1,'a'):one, (1,'b'):one, (2,'a'):one, (2,'c'):one, (3,'a'):one, (3,'c'):one, (3,'d'):one,})
    b = Vec({'a','b','c','d'}, {'a':one, 'c':one})
    U = M*A
    col_label_list = sorted(A.D[1])
    U_rows_dict = mat2rowdict(U)
    row_list = [U_rows_dict[i] for i in sorted(U_rows_dict)]
    print(row_list)
    print()
    print(col_label_list)
    print()
    print(M*b)

# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

def main():
    os.system('clear')
    print('\n')
    print('------problem7------')
    problem7()
    print('\n')

# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

if __name__ == '__main__':
    main()


