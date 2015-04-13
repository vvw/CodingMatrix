from mat import Mat
from vec import Vec
from vecutil import list2vec
from matutil import listlist2mat, coldict2mat
from solver import solve


def problem2():
    T = Mat((set([0, 1, 2, 3]), set([0, 1, 2, 3])), {(0, 1): 0.25, (1, 2): 0.0, (3, 2): 0, (0, 0): 1, (3, 3): 1, (3, 0): 0, (3, 1): 0, (2, 1): 0, (0, 2): 0.75, (2, 0): 0, (1, 3): -0.25, (2, 3): 0, (2, 2): 1, (1, 0): 0, (0, 3): 0.5, (1, 1): 1})
    b1 = Vec({0, 1, 2, 3}, {2: 1})
    b2 = Vec({0, 1, 2, 3}, {3: 1})
    print(T)
    print(b1)
    print(b2)
    x1 = solve(T, b1)
    x2 = solve(T, b2)
    
    print([x1,x2])
    
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

if __name__ == '__main__':
    problem2()




