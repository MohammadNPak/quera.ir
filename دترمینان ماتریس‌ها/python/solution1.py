
# https://quera.ir/problemset/608/
from typing import List


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

    def det(self):
        # from copy import deepcopy
        # if len(matrix_data) == 2:
        #     return matrix_data[0][0]*matrix_data[1][1]-matrix_data[0][1]*matrix_data[1][0]
        # elif len(matrix_data) == 1:
        #     return matrix_data[0][0]
        # else:
        #     sign = 1
        #     det = 0

        #     for index, c in enumerate(matrix_data[0]):
        #         # new_data2 = new_data1.copy()
        #         new_data1 = deepcopy(matrix_data[1:])
        #         for i in range(len(matrix_data)-1):
        #             del new_data1[i][index]

        #         det += sign*c * self.det(new_data1)
        #         sign *= -1
        #     return float(det)
        def determinant(data):
            if len(data) == 2 and len(data[0]) == 2 and len(data[1]) == 2:
                return data[0][0]*data[1][1] - data[0][1]*data[1][0]
            elif len(data) == 1:
                return float(data[0][0])
            else:
                det = 0
                sign = 1
                for i, c in enumerate(data[0]):
                    if c == 0:
                        continue
                    else:
                        det += sign*c * determinant(
                            [[x[y] for y in range(len(x)) if y != i]
                             for x in data[1:]]
                        )
                        sign *= -1
                return det

        return determinant(self.data)


# n = int(input())
# data = []
# for i in range(n):
#     data.extend([float(x) for x in input().split()])
# m1 = Matrix(data, n, n)
# print(round(m1.det(), 2))


def determinant(data):
    if len(data) == 2 and len(data[0]) == 2 and len(data[1]) == 2:
        return data[0][0]*data[1][1] - data[0][1]*data[1][0]
    elif len(data) == 1:
        return float(data[0][0])
    else:
        det = 0
        sign = 1
        for i, c in enumerate(data[0]):
            if c == 0:
                continue
            else:
                det += sign*c * determinant(
                    [[x[y] for y in range(len(x)) if y != i]
                     for x in data[1:]]
                )
                sign *= -1
        return det


data = []
n = int(input())
for _ in range(n):
    data.append([float(x) for x in input().split()])

print(f"{round(determinant(data), 2):.2f}")
