# 杨辉三角

def triangles():
    L = [1]
    while True:
        yield L
        M = L[:]
        M.append(0)
        L = [M[i-1]+M[i] for i in range(len(M))]


def result_print(n=10):
    i = 0
    # result = []
    for t in triangles():
        print(t)
        # result.append(t)
        # print(result)
        i += 1
        if i == n:
            break


if __name__ == '__main__':
    result_print()