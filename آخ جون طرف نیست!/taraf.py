w = {'shanbe', '1shanbe', '2shanbe', '3shanbe', '4shanbe', '5shanbe', 'jome'}
for i in range(1, 4):
    n = int(input())
    l = input().split()
    l = set(l)
    w = w-l
print(len(w))
