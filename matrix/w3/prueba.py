from vec import Vec
from mat import Mat
from bitutil import bits2mat, str2bits, noise
from GF2 import one
from matutil import listlist2mat

def find_error(syndrome):
    """
    Input: an error syndrome as an instance of Vec
    Output: the corresponding error vector e
    Examples:
        >>> find_error(Vec({0,1,2}, {0:one})) == Vec({0, 1, 2, 3, 4, 5, 6},{3: one})
        True
        >>> find_error(Vec({0,1,2}, {2:one})) == Vec({0, 1, 2, 3, 4, 5, 6},{0: one})
        True
        >>> find_error(Vec({0,1,2}, {1:one, 2:one})) == Vec({0, 1, 2, 3, 4, 5, 6},{2: one})   
        True
        >>> find_error(Vec({0,1,2}, {})) == Vec({0,1,2,3,4,5,6}, {})
        True
    """
    if len(syndrome.f) > 0:
        f = lambda x: {0:4, 1:2, 2:1}[x]
        posval = sum(f(x) for x in syndrome.f)
        return Vec({0,1,2,3,4,5,6}, {(posval-1): one})
    return Vec({0,1,2,3,4,5,6}, {})

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print(find_error(Vec({0,1,2}, {0:one})) == Vec({0, 1, 2, 3, 4, 5, 6},{3: one}))
    print(find_error(Vec({0,1,2}, {2:one})) == Vec({0, 1, 2, 3, 4, 5, 6},{0: one}))
    print(find_error(Vec({0,1,2}, {1:one, 2:one})) == Vec({0, 1, 2, 3, 4, 5, 6},{2: one}))
    print(find_error(Vec({0,1,2}, {})) == Vec({0,1,2,3,4,5,6}, {}))
