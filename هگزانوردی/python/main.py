
# https://quera.ir/problemset/127291/


# a => a
# b => b
# c => c
# d => -a
# e => -b
# f => -c


t = int(input())
answers = []
for i in range(t):
    s:str = input()
    a = s.count('A') - s.count('D')
    b = s.count('B') - s.count('E')
    c = s.count('C') - s.count('F')
    
    s = abs(a)+abs(b)+abs(c)
    while True:    
        if a>0 and c>0:
            x = min(a,c)
            a,b,c = a-x,b+x,c-x
        elif a<0 and c<0:
            x = max(a,c)
            a,b,c = a-x,b+x,c-x
        elif a>0 and b <0:
            x = min(a,-b)
            a,b,c = a-x,b+x,c-x
        elif b>0 and a<0:
            x = min(b,-a)
            a,b,c = a+x,b-x,c+x
        elif b>0 and c<0:
            x = min(b,-c)
            a,b,c = a+x,b-x,c+x
        elif c>0 and b <0:
            x = min(c,-b)
            a,b,c = a-x,b+x,c-x
        
        new_s = abs(a)+abs(b)+abs(c)
        if  new_s == s:
            answers.append(new_s)
            break
        else:
            s = new_s

for  answer in answers:
    print(answer)
