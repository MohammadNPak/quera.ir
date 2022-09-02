# https://quera.org/problemset/66867/

n,m = input().split()
n,m = int(n),int(m)

w_counter = [0 for k in range(n)]
for i in range(m):
    colors = input()
    for j in range(n):
        if colors[j]=="W":
            w_counter[j]+=1

output_list = ["F" if x%2!=0 else "B" for x in w_counter]
print("".join(output_list))

