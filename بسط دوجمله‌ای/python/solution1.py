# https://quera.org/problemset/220670

from math import comb
n = int(input())

def convert(coefficient,base,power):
    if coefficient==0:
        return ""
    if coefficient==1:
        coefficient=""
    if power==0:
        return str(coefficient)
    elif power==1:
        return f"{coefficient}{base}"
    elif power>=10:
        return f"{coefficient}{base}^{{{power}}}"
    else:
        return f"{coefficient}{base}^{power}"
output=[]
for i in range(n+1):
    output.append((
        convert(comb(n,i),"x",n-i)+
        convert(1,"y",i)
        )
    )
print("+".join(output))

