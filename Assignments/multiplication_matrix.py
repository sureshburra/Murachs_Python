matrix1 = [
    [1, 2, 3],
    [2, 3, 4],
    [1, 1, 1]
]

matrix2 = [
    [4, 5, 6],
    [7, 8, 9],
    [4, 5, 7]
]

result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(3):
    for j in range(3):
        for k in range(3):
            result[i][j] += matrix1[i][k] * matrix2[k][j]

A = result[0][0]
B = result[0][1]
C = result[0][2]
D = result[1][0]
E = result[1][1]
F = result[1][2]
G = result[2][0]
H = result[2][1]
I = result[2][2]

print(A, B, C, D, E, F, G, H, I, sep='\n')