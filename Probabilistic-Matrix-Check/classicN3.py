def classicCheckMultiply(A, B, C):

    size = len(A)

    M = [[0] * size for _ in range(size)]

    for i in range(0, size):
        m = [0] * size
        for j in range(0, size):
            new = 0
            for k in range(0, size):
                new += A[i][k] * B[k][j]
            m[j] = new
        M[i] = m

    check = "YES"
    for i in range(0, size):
        for j in range(0, size):
            if M[i][j] != C[i][j]:
                check = "NO"
                break

    return check