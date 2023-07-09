def pascal_triangle(rows):
    triangle = []

    for i in range(rows):
        row = []

        for j in range(i+1):
            if j == 0 or j == 1:
                row.append(1)
            else:
                value = triangle[i-1][j-1] + triangle[i-1][j]
                row.append(val)
        triangle.append(row)
    return triangle