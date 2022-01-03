# https://quera.ir/problemset/607/

a, b, c = input().split()
a, b, c = int(a), int(b), int(c)

m1, n1 = a, b
m2, n2 = b, c
m3, n3 = m1, n2
A = []
B = []
C = []
# my_list = []
# for i in range(10):
#     my_list.append(i**2)
# my_list= [x**2 for x in range(10)]
for _ in range(m1):
    row = [int(x) for x in input().split()]
    A.append(row)

# A = [
#     [1,2,3],
#     [4,5,6],
#             ]
for _ in range(m2):
    row = [int(x) for x in input().split()]
    B.append(row)

for i in range(m3):
    C_row = []
    for j in range(n3):
        # cij=?
        row = A[i]
        col = [x[j] for x in B]
        c = sum([x*y for x, y in zip(row, col)])
        C_row.append(c)
    C.append(C_row)

# A = [1, 2, 3]
# B = [10,20,30]
# for a,b in zip(A,B):
#     print(a,b)
for i in range(len(C)):
    for j in range(len(C[0])):
        print(C[i][j], end=" ")
    print("\n")