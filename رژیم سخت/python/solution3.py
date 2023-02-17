rejim = input()
red = rejim.count('R')
yellow = rejim.count('Y')
green = rejim.count('G')
if red >= 3:
    print('nakhor lite')
elif red >= 2 and yellow >= 2:
    print('nakhor lite')
elif green == 0:
    print('nakhor lite')
else:
    print('rahat baash')
