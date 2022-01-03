# https://quera.ir/problemset/66862/
from itertools import accumulate, product
s = input()


def check_validity(x):
    if sum(x) != len(s):
        return False
    y = list(accumulate(x))
    for i in range(4):
        if i == 0:
            octave = s[:y[i]]
        else:
            octave = s[y[i-1]:y[i]]
        if int(octave) > 255:
            return False
        elif octave[0] == '0' and len(octave) != 1:
            return False

    return True


a = product([1, 2, 3], repeat=4)
# print(a)
for b in filter(check_validity, a):
    octave = []
    b = list(accumulate(b))
    print(s[:b[0]], s[b[0]:b[1]], s[b[1]:b[2]], s[b[2]:b[3]], sep='.')
