# https://quera.org/problemset/220671


def P(loop_number):
    if loop_number==0:
        return 0
    elif loop_number==1:
        return 1
    else:
        return 1+2*loop_number*(loop_number-1)

def calculate(x,y):
    if x==0 and y==0:
        return 1
    
    ln=abs(x)+abs(y)
    if x>=0 and y>0:
        return P(ln)+x+1
    elif x>0 and y<=0:
        return P(ln)+ln+abs(y)+1
    elif x<=0 and y <0:
        return P(ln)+2*ln+abs(x)+1
    elif x<0 and y>=0:
        return P(ln)+3*ln+abs(y)+1

output=[]
t = int(input())
for i in range(t):
    x,y = map(int,input().split())
    output.append(calculate(x,y))

for i in output:
    print(i)