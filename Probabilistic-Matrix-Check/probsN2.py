import random

def probsCheckMultiply(A, B, C):
    size = len(A)
    pList = [22801763489, 23050700011, 23333333333, 23457987601, 23765203727,
         24124140487, 24571243009, 24682022243, 25505418241, 25707225491]
    p = random.choice(pList)
    x = [(random.randint(0, p)) for _ in range(size)]

    m = [0] * size
    for i in range(0, size):
        for j in range(0, size):
            m[i] += B[i][j] * x[j]
        m[i] = m[i]
    n = [0] * size
    for i in range(0, size):
        for j in range(0, size):
            n[i] += A[i][j] * m[j]
        n[i] = n[i] % p

    k = [0] * size
    for i in range(0, size):
        for j in range(0, size):
            k[i] += C[i][j] * x[j]
        k[i] = k[i] % p

    for i in range(0, size):
        if n[i] != k[i]:
            return "NO"
    return "YES"
