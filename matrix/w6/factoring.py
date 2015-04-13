
from factoring_lab import *
from vec import Vec
from GF2 import one
from matutil import mat2rowdict

from factoring_support import dumb_factor
from factoring_support import intsqrt
from factoring_support import gcd
from factoring_support import primes
from factoring_support import prod

def problem3():
    a, b = find_candidates(2419, primes(32))
    print(a)
    print(b)

# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

def problem4():
    roots = [51, 52, 53, 58, 61, 62, 63, 67, 68, 71, 77, 79]
    N = 2419
    v = Vec({0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11},{1: one, 2: one, 11: one, 5: one})  
    print(find_a_and_b(v, roots, N))
    print('~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~')
    v = Vec({0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11},{0: 0, 1: 0, 10: one, 2: one})
    print(find_a_and_b(v, roots, N))

# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

def gcd(x,y): return x if y == 0 else gcd(y, x % y)

def problem5():
    N = 2461799993978700679
    print('generando primelist ...')
    primelist = primes(10000)
    print('buscando candidatos ...')
    roots, rowlist = find_candidates(N, primelist)
    print('calculando M ...')
    M = echelon.transformation_rows(rowlist)
    print('extraccion de v ...')
    v = M[-2]
    print('busqueda de a y b ...')
    a, b = find_a_and_b(v, roots, N)
    amb = a - b
    print('buscando gcd ...')
    print(gcd(amb, N))

# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

def main():
    problem5()
    

# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

if __name__ == '__main__':
    main()


