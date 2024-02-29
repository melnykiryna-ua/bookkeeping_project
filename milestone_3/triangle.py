import sys


def get_triangle(rows):
    triangle = []
    for i in range(rows):
        row = [1] * (i+1)
        triangle.append(row)

    for i in range(2, rows):
        for j in range(1, i):
            triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]

    return triangle


try:
    rows = int(sys.argv[1])
except:
    rows = 0
    print("Wrong input")

triangle = get_triangle(rows)
for row, i in zip(triangle, range(len(triangle), 0, -1)):
    print(" " * i, *row)
