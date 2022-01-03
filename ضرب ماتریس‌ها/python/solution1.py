# https://quera.ir/problemset/607/


from typing import List, Sequence


class Matrix:
    def __init__(self, data: List, m: int, n: int) -> None:
        """
        for matrix [ 1 2 3
                     4 5 6
                     7 8 9]
        data = [1,2,3,4,5,6,7,8,9]
        """
        self.rows = m
        self.cols = n
        self.data = []
        if len(data) != m*n:
            raise Exception("data size must be  equal to m*n")
        else:
            for i in range(0, m*n, n):
                self.data.append(data[i:i+n])

    def __str__(self) -> str:
        output = ""
        for row in self.data:
            # output += "|"
            for element in row:
                output += f"{element} "
            # output += "|\n"
            output += "\n"
        return output

    def __mul__(self, other):
        if self.cols != other.rows:
            raise Exception(
                "cols of left matrix must be equal to rows of right matrix")
        else:
            output = []
            for i in range(self.rows):
                row = []
                for j in range(other.cols):
                    c_ij = 0
                    for index, element in enumerate(self.data[i]):
                        c_ij += element*other.data[index][j]
                    output.append(c_ij)
                # output.append(row)
            output_matrix = Matrix(output, self.rows, other.cols)
            return output_matrix


a, b, c = input().split()
a, b, c = int(a), int(b), int(c)
A = []
for _ in range(a):
    A.extend(input().split())
B = []
for _ in range(b):
    B.extend(input().split())

A = [int(x) for x in A]
B = [int(x) for x in B]
m1 = Matrix(A, a, b)
m2 = Matrix(B, b, c)
m3 = m1*m2
print(m3)
