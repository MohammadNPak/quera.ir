# https://quera.org/problemset/2529/

n = int(input())
names = []
for i in range(n):
  names.append(len(set(input())))
print(max(names))