from typing import List

matrix:List[List[int]] = [
    [1,0,1],
    [0,0,0],
    [1,1,0]
]

def rotate(matrix:List[List[int]])->List[List[int]]:
    N:int = len(matrix)
    matrix_rotate:List[List[int]] = []
    for i in range(N):
        new_matrix:List[int] = []
        for j in range(N-1, -1, -1):
            new_matrix.append(matrix[j][i])
        matrix_rotate.append(new_matrix)
    return matrix_rotate


def mirror(matrix:List[List[int]])->List[List[int]]:
    N = len(matrix)
    mirror_matrix:List[List[int]] = []
    for i in range(N):
        new_matrix:List[int] = []
        for j in range(N-1, -1, -1):
            new_matrix.append(matrix[i][j])
        mirror_matrix.append(new_matrix)
    return mirror_matrix

print(mirror(matrix=matrix))