# https://quera.org/problemset/17675/

N = int(input())

n=1
fn_1=1
fn=1
output = []
while fn <=N:
  output.append(fn)
  fn,fn_1 =fn+fn_1,fn 

s=["-"]*N
for i in range(1,N+1):
  if i in output:
    s[i-1]="+"
print("".join(s))