# https://quera.org/problemset/220669/

n,m = map(int,input().split())
output=[0]*n
result = []
for i in range(m):
    s,l = map(int,input().split())
    start = s-1
    end = start
    while start <n and end <n:
        if output[end]==0:
            if end-start+1==l:
                output[start:end+1]=[1]*l
                break
            end+=1
        else:
            start=end+1
            end=start
    result.append("".join(map(str,output)))

for i in result:
    print(i)
