from GF2 import one, One
from math import sqrt, pi
from matutil import coldict2mat
from solver import solve
from vec import Vec
from vecutil import list2vec

def exchange(S, A, z):
    '''
    Input:
        - S: a set of Vecs (not necessarily linearly independent)
        - A: a set of Vecs, a proper subset of S
        - z: an instance of Vec such that A | {z} is linearly independent
    Output: a vector w in S but not in A such that Span S = Span ({z} | S - {w})
    Examples:
        >>> from vecutil import list2vec
        >>> from vec import Vec
        >>> S = {list2vec(v) for v in [[0,0,5,3],[2,0,1,3],[0,0,1,0],[1,2,3,4]]}
        >>> A = {list2vec(v) for v in [[0,0,5,3],[2,0,1,3]]}
        >>> z = list2vec([0,2,1,1])
        >>> (exchange(S, A, z) == Vec({0, 1, 2, 3},{0: 0, 1: 0, 2: 1, 3: 0})) or (exchange(S, A, z) == Vec({0, 1, 2, 3},{0: 1, 1: 2, 2: 3, 3: 4}))
        True
        >>> S == {list2vec(v) for v in [[0,0,5,3],[2,0,1,3],[0,0,1,0],[1,2,3,4]]}
        True
        >>> A == {list2vec(v) for v in [[0,0,5,3],[2,0,1,3]]}
        True
        >>> z == list2vec([0,2,1,1])
        True
        >>> from GF2 import one
        >>> S = {Vec({0,1,2,3,4}, {i:one, (i+1)%5:one}) for i in range(5)}
        >>> A = {list2vec([0,one,one,0,0]),list2vec([0,0,one,one,0])}
        >>> z = list2vec([0,0,one,0,one])
        >>> exchange(S, A, z) in {list2vec(v) for v in [[one, one,0,0,0],[one,0,0,0,one],[0,0,0,one,one]]}
        True
        >>> S = {list2vec(v) for v in [[one,0,one,0],[one,one,one,one],[one,one,0,0],[one,one,one,0]]}
        >>> A = {list2vec([one,one,one,0])}
        >>> z = list2vec([0,one,0,0])
        >>> exchange(S, A, z) == list2vec([one,0,one,0])
        True
        >>> S = {list2vec(v) for v in [[0,0,0,one,0],[one,0,0,0,one],[one,0,one,one,one],[0,one,one,one,one],[one,one,one,0,0],[one,one,0,0,one]]}
        >>> A = {list2vec(v) for v in [[one,0,0,0,one],[0,one,one,one,one],[0,0,0,one,0],[one,one,one,0,0]]}
        >>> z = list2vec([0,one,0,one,one])
        >>> exchange(S, A, z) == list2vec([one,0,one,one,one])
        True
    '''
    basis = coldict2mat(list(S))
    rep = solve(basis, z)

    for alpha, col in zip(rep, basis.D[1]):
        if alpha != 0:
            new_v = Vec(z.D, {i:basis[row,col] for i, row in zip(z.D, basis.D[0])})
            if new_v not in A:
                return (new_v / alpha)
            
    


if __name__ == '__main__':
    S = {list2vec(v) for v in [[0,0,5,3],[2,0,1,3],[0,0,1,0],[1,2,3,4]]}
    A = {list2vec(v) for v in [[0,0,5,3],[2,0,1,3]]}
    z = list2vec([0,2,1,1])
    print((exchange(S, A, z) == Vec({0, 1, 2, 3},{0: 0, 1: 0, 2: 1, 3: 0})) or (exchange(S, A, z) == Vec({0, 1, 2, 3},{0: 1, 1: 2, 2: 3, 3: 4})))
    print(S == {list2vec(v) for v in [[0,0,5,3],[2,0,1,3],[0,0,1,0],[1,2,3,4]]})
    print(A == {list2vec(v) for v in [[0,0,5,3],[2,0,1,3]]})
    print(z == list2vec([0,2,1,1]))
    print('-------------')
    S = {Vec({0,1,2,3,4}, {i:one, (i+1)%5:one}) for i in range(5)}
    A = {list2vec([0,one,one,0,0]),list2vec([0,0,one,one,0])}
    z = list2vec([0,0,one,0,one])
    print(exchange(S, A, z) in {list2vec(v) for v in [[one, one,0,0,0],[one,0,0,0,one],[0,0,0,one,one]]})
    S = {list2vec(v) for v in [[one,0,one,0],[one,one,one,one],[one,one,0,0],[one,one,one,0]]}
    A = {list2vec([one,one,one,0])}
    z = list2vec([0,one,0,0])
    print(exchange(S, A, z) == list2vec([one,0,one,0]))
    S = {list2vec(v) for v in [[0,0,0,one,0],[one,0,0,0,one],[one,0,one,one,one],[0,one,one,one,one],[one,one,one,0,0],[one,one,0,0,one]]}
    A = {list2vec(v) for v in [[one,0,0,0,one],[0,one,one,one,one],[0,0,0,one,0],[one,one,one,0,0]]}
    z = list2vec([0,one,0,one,one])
    print(exchange(S, A, z) == list2vec([one,0,one,one,one]))
    print('--------------')
    D = {0,1,2,3,4}
    S = {Vec(D,{0: one, 1: one, 2: one, 4: one}), Vec(D,{1: one, 2: one, 3: one}), Vec(D,{0: one, 1: one, 4: one}), Vec(D,{4: one}), Vec(D,{1: one})}
    A = {Vec(D,{1: one, 2: one, 3: one}), Vec(D,{4: one}), Vec(D,{1: one})}
    z = Vec(D,{0: one, 3: one, 4: one})
    print(exchange(S, A, z)== Vec(D,{0: one, 1: one, 2: one, 4: one}))
    
