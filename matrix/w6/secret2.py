import random
from GF2 import one
from vecutil import list2vec
from independence import is_independent

a0 = list2vec([one, one,   0, one,   0, one])
b0 = list2vec([one, one,   0,   0,   0, one])

def bin2vect(n):
    num = bin(n)
    bin_list = [ one if x == '1' else 0 for x in num[2:]]
    if len(bin_list) < 6:
        new_lst = [0] * (6 - len(bin_list))
        new_lst.extend(bin_list)
        return list2vec(new_lst)
    return list2vec(bin_list)

def main(m):
    cont = 0
    while True:
        cont += 1
        print('... VUELTA {} ...'.format(cont))
        vecs = list(range(64))
        ab_list = [a0, b0]
        while True:
            if len(vecs) > 0:
                rnd = random.randint(0, len(vecs)-1)
                new_v = bin2vect(vecs.pop(rnd))
                if is_independent(ab_list + [new_v]):
                    ab_list.append(new_v)
                    if len(ab_list) > m:
                        return ab_list
                print('rnd:{}, len:{}, vecs:{}'.format(rnd, len(ab_list), len(vecs)))
            else:
                break

if __name__ == '__main__':
    a = main(6)
    print(a)


