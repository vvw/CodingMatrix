# version code 7f08c507c12c+
coursera = 1
# Please fill out this stencil and submit using the provided submission script.
from math import sqrt
from mat import Mat
from vec import Vec
from vecutil import list2vec
from matutil import listlist2mat, mat2rowdict



## 1: (Problem 1) Generators for orthogonal complement
U_vecs_1 = [list2vec([0,0,3,2])]
W_vecs_1 = [list2vec(v) for v in [[1,2,-3,-1],[1,2,0,1],[3,1,0,-1],[-1,-2,3,1]]]
# Give a list of Vecs
ortho_compl_generators_1 = [list2vec(v) for v in [[1,2,-0.4615384615384617,0.6923076923076923],[2.2432432432432434, -0.5135135135135134, 0.811, -1.2162162162162162]]]

U_vecs_2 = [list2vec([3,0,1])]
W_vecs_2 = [list2vec(v) for v in [[1,0,0],[1,0,1]]]

# Give a list of Vecs
ortho_compl_generators_2 = [list2vec([0.1,0,-0.3])]

U_vecs_3 = [list2vec(v) for v in [[-4,3,1,-2],[-2,2,3,-1]]]
W_vecs_3 = [list2vec(v) for v in [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]]

# Give a list of Vecs
ortho_compl_generators_3 = [list2vec(v) for v in [[0.419,0.391,-0.0782,-0.291],[0,0.333,-0.0667,0.467]]]



## 2: (Problem 2) Basis for null space
# Your solution should be a list of Vecs
null_space_basis = [Vec({0, 1, 2, 3},{0: -0.75, 1: 0.0, 2: 1.0, 3: 0.0}), Vec({0, 1, 2, 3},{0: -0.5625, 1: 0.25, 2: 0.0, 3: 1.0})]



## 3: (Problem 3) Orthonormalize(L)
def project_along(b,v):
    sigma = (b*v)/(v*v)
    return sigma*v

def project_orthogonal(b, vlist):
    for v in vlist:
        b = b - project_along(b,v)
    return b

def orthogonalize(vlist):
    vstarlist = []
    for v in vlist:
        vstarlist.append(project_orthogonal(v, vstarlist))
    return vstarlist

def orthonormalize(L):
    '''
    Input: a list L of linearly independent Vecs
    Output: A list Lstar of len(L) orthonormal Vecs such that, for all i in range(len(L)),
            Span L[:i+1] == Span Lstar[:i+1]

    >>> from vec import Vec
    >>> D = {'a','b','c','d'}
    >>> L = [Vec(D, {'a':4,'b':3,'c':1,'d':2}), Vec(D, {'a':8,'b':9,'c':-5,'d':-5}), Vec(D, {'a':10,'b':1,'c':-1,'d':5})]
    >>> for v in orthonormalize(L): print(v)
    ... 
    <BLANKLINE>
        a     b     c     d
    -----------------------
     0.73 0.548 0.183 0.365
    <BLANKLINE>
         a     b      c      d
    --------------------------
     0.187 0.403 -0.566 -0.695
    <BLANKLINE>
         a      b      c     d
    --------------------------
     0.528 -0.653 -0.512 0.181
    '''
    vstar = orthogonalize(L)
    norm = [sqrt(v*v) for v in vstar]
    return [v/n for v, n in zip(vstar, norm)]



## 4: (Problem 4) aug_orthonormalize(L)
def aug_project_orthogonal(b, vlist):
    alphadict = dict()
    if len(vlist) == 0:
        alphadict[0] = 1
    else:
        for i, v in enumerate(vlist):
            sigma = (b*v)/(v*v) if (v*v) != 0 else 0
            alphadict[i] = sigma
            b = b - sigma*v
        alphadict[i+1] = 1
    return b, alphadict

def aug_orthogonalize(vlist):
    vstarlist = []
    r_vecs = []
    D = set(range(len(vlist)))
    for v in vlist:
        (vstar, alphadict) = aug_project_orthogonal(v, vstarlist)
        vstarlist.append(vstar)
        r_vecs.append(Vec(D, alphadict))
    return vstarlist, r_vecs

def aug_orthonormalize(L):
    '''
    Input:
        - L: a list of Vecs
    Output:
        - A pair Qlist, Rlist such that:
            * coldict2mat(L) == coldict2mat(Qlist) * coldict2mat(Rlist)
            * Qlist = orthonormalize(L)
            
    >>> from vec import Vec
    >>> D={'a','b','c','d'}
    >>> L = [Vec(D, {'a':4,'b':3,'c':1,'d':2}), Vec(D, {'a':8,'b':9,'c':-5,'d':-5}), Vec(D, {'a':10,'b':1,'c':-1,'d':5})]
    >>> Qlist, Rlist = aug_orthonormalize(L)
    >>> from matutil import coldict2mat
    >>> print(coldict2mat(Qlist))
    <BLANKLINE>
               0      1      2
         ---------------------
     a  |   0.73  0.187  0.528
     b  |  0.548  0.403 -0.653
     c  |  0.183 -0.566 -0.512
     d  |  0.365 -0.695  0.181
    <BLANKLINE>
    >>> print(coldict2mat(Rlist))
    <BLANKLINE>
              0    1      2
         ------------------
     0  |  5.48 8.03   9.49
     1  |     0 11.4 -0.636
     2  |     0    0   6.04
    <BLANKLINE>
    >>> print(coldict2mat(Qlist)*coldict2mat(Rlist))
    <BLANKLINE>
           0  1  2
         ---------
     a  |  4  8 10
     b  |  3  9  1
     c  |  1 -5 -1
     d  |  2 -5  5
    <BLANKLINE>
    '''
    Qlist, Rlist = aug_orthogonalize(L)
    norm = [sqrt(v*v) for v in Qlist]
    normQlist = [v/n for v, n in zip(Qlist, norm)]
    normRlist = []
    for r in Rlist:
        normRlist.append(Vec(r.D,{i:r[i]*norm[i] for i in r.D}))
    return normQlist, normRlist



## 5: (Problem 5) QR factorization of small matrices
#Compute the QR factorization

#Please represent your solution as a list of rows, such as [[1,0,0],[0,1,0],[0,0,1]]

part_1_Q = [[0.857,0.256],[0.286,-0.958],[0.429,0.128]]
part_1_R = [[7,6.43],[0,1.92]]

part_2_Q = [[0.667,0.707],[0.667,-0.707],[0.333,0]]
part_2_R = [[3,3],[0,1.41]]



## 6: (Problem 6) QR Solve
from matutil import mat2coldict, coldict2mat
from python_lab import dict2list, list2dict
from triangular import triangular_solve

def QR_factor(A):
    col_labels = sorted(A.D[1], key=repr)
    Acols = dict2list(mat2coldict(A),col_labels)
    Qlist, Rlist = aug_orthonormalize(Acols)
    #Now make Mats
    Q = coldict2mat(Qlist)
    R = coldict2mat(list2dict(Rlist, col_labels))
    return Q,R


def QR_solve(A, b):
    '''
    Input:
        - A: a Mat with linearly independent columns
        - b: a Vec whose domain equals the set of row-labels of A
    Output:
        - vector x that minimizes norm(b - A*x)
    Note: This procedure uses the procedure QR_factor, which in turn uses dict2list and list2dict.
           You wrote these procedures long back in python_lab.  Make sure the completed python_lab.py
           is in your matrix directory.
    Example:
        >>> domain = ({'a','b','c'},{'A','B'})
        >>> A = Mat(domain,{('a','A'):-1, ('a','B'):2,('b','A'):5, ('b','B'):3,('c','A'):1,('c','B'):-2})
        >>> Q, R = QR_factor(A)
        >>> b = Vec(domain[0], {'a': 1, 'b': -1})
        >>> x = QR_solve(A, b)
        >>> result = A.transpose()*(b-A*x)
        >>> result.is_almost_zero()
        True
    '''
    Q, R = QR_factor(A)
    c = Q.transpose() * b
    #return solve(R, c)
    return triangular_solve(mat2rowdict(R), sorted(A.D[1], key=repr), c)



## 7: (Problem 7) Least Squares Problem
# Please give each solution as a Vec

least_squares_A1 = listlist2mat([[8, 1], [6, 2], [0, 6]])
least_squares_Q1 = listlist2mat([[.8,-0.099],[.6, 0.132],[0,0.986]])
least_squares_R1 = listlist2mat([[10,2],[0,6.08]])
least_squares_b1 = list2vec([10, 8, 6])

x_hat_1 = list2vec([1.0832432432432433, 0.9837837837837838])


least_squares_A2 = listlist2mat([[3, 1], [4, 1], [5, 1]])
least_squares_Q2 = listlist2mat([[.424, .808],[.566, .115],[.707, -.577]])
least_squares_R2 = listlist2mat([[7.07, 1.7],[0,.346]])
least_squares_b2 = list2vec([10,13,15])

x_hat_2 = list2vec([2.499999999999997, 2.6666666666666776])



## 8: (Problem 8) Small examples of least squares
#Find the vector minimizing (Ax-b)^2

#Please represent your solution as a list

your_answer_1 = [1.0832432432432433, 0.9837837837837838]
your_answer_2 = [3.000000000000015, 0.9999999999999476]



## 9: (Problem 9) Linear regression example
#Find a and b for the y=ax+b line of best fit

a = 0.6349650349650352
b = 64.928321678321666

