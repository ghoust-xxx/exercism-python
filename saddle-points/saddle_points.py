def saddle_points(matrix):
    mat = [ [False] * len(matrix[0]) for i in range(0, len(matrix)) ]
    res = []
    if len(matrix) == 0:
        return res
    for i in range(0, len(matrix)):
        max_val = matrix[i][0]
        if len(matrix[i]) != len(matrix[0]):
            raise ValueError("irregular matrix")
        for j in range(0, len(matrix[i])):
            if matrix[i][j] > max_val:
                max_val = matrix[i][j]
        for j in range(0, len(matrix[i])):
            if matrix[i][j] == max_val:
                mat[i][j] = True
    for j in range(0, len(matrix[0])):
        min_val = matrix[0][j]
        for i in range(0, len(matrix)):
            if matrix[i][j] < min_val:
                min_val = matrix[i][j]
        for i in range(0, len(matrix)):
            if matrix[i][j] != min_val:
                mat[i][j] = False

    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            if mat[i][j] == True:
                res.append({"row": i+1, "column": j+1})

    return res
