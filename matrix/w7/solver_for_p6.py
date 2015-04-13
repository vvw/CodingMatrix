from math import sqrt
from mat import Mat
from vec import Vec
from vecutil import list2vec
from matutil import listlist2mat
from Orthogonalization_problems import *
from read_data import read_vectors

def problem6():
    domain = ({'a','b','c'},{'A','B'})
    A = Mat(domain,{('a','A'):-1, ('a','B'):2,('b','A'):5, ('b','B'):3,('c','A'):1,('c','B'):-2})
    print(A)
    Q, R = QR_factor(A)
    print(Q)
    print(R)
    b = Vec(domain[0], {'a': 1, 'b': -1})
    x = QR_solve(A, b)
    print(x)
    print([x])
    result = A.transpose()*(b-A*x)
    print(result.is_almost_zero())

# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

def problem7_1():
    domain = ({'a','b','c'},{'A','B'})
    A = Mat(domain,{('a','A'):8, ('a','B'):1,('b','A'):6, ('b','B'):2,('c','A'):0,('c','B'):6})
    print(A)
    b = Vec(domain[0], {'a': 10, 'b': 8, 'c': 6})
    print(b)
    x = QR_solve(A, b)
    print(x)
    print([x])
    result = A.transpose()*(b-A*x)
    print(result.is_almost_zero())
    print((b-A*x)*(b-A*x))

# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

def problem7_2():
    domain = ({'a','b','c'},{'A','B'})
    A = Mat(domain,{('a','A'):3, ('a','B'):1,('b','A'):4, ('b','B'):1,('c','A'):5,('c','B'):1})
    print(A)
    b = Vec(domain[0], {'a': 10, 'b': 13, 'c': 15})
    print(b)
    x = QR_solve(A, b)
    print(x)
    print([x])
    result = A.transpose()*(b-A*x)
    print(result.is_almost_zero())
    print((b-A*x)*(b-A*x))

# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

def problem8_1():
    domain = ({'a','b','c'},{'A','B'})
    A = Mat(domain,{('a','A'):8, ('a','B'):1,('b','A'):6, ('b','B'):2,('c','A'):0,('c','B'):6})
    print(A)
    b = Vec(domain[0], {'a': 10, 'b': 8, 'c': 6})
    print(b)
    x = QR_solve(A, b)
    print(x)
    print([x])
    result = A.transpose()*(b-A*x)
    print(result.is_almost_zero())
    print((b-A*x)*(b-A*x))

# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

def problem8_2():
    domain = ({'a','b'},{'A','B'})
    A = Mat(domain,{('a','A'):3, ('a','B'):1,('b','A'):4, ('b','B'):1})
    print(A)
    b = Vec(domain[0], {'a': 10, 'b': 13})
    print(b)
    x = QR_solve(A, b)
    print(x)
    print([x])
    result = A.transpose()*(b-A*x)
    print(result.is_almost_zero())
    print((b-A*x)*(b-A*x))

# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

def problem9():
    vlist = read_vectors('age-height.txt')
    agelist = []
    heightlist = []
    for v in vlist:
        agelist.append(v['age'])
        heightlist.append(v['height'])
    oneslist = [1] * len(agelist)
    print(agelist)
    print(heightlist)
    colsA = [[a, o] for a, o in zip(agelist, oneslist)]
    A = listlist2mat(colsA)
    print(A)
    b = list2vec(heightlist)
    print(b)
    x = QR_solve(A, b)
    print(x)
    result = A.transpose()*(b-A*x)
    print(result.is_almost_zero())

# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

def main():
    problem9()

# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

if __name__ == '__main__':
    main()


