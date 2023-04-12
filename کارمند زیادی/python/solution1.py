# https://quera.org/problemset/10636/

names=[]
for i in range(int(input())):
    names.append(input().split()[0])
unique_names={name:names.count(name) for name in set(names)}
print(max(unique_names.values()))
        

