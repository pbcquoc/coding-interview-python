import math
import queue

def is_possible(m, n, k, r, X, Y):
    rect = [[0]*n for i in range(m)]

    for i in range(m):
        for j in range(n):
            for p in range(k):
                if math.sqrt((pow((X[p] -1 -i), 2) + pow((Y[p] -1 -j), 2))) <= r:
                    rect[i][j] = -1

    
    if rect[0][0] == -1:
        return False

    qu = queue.Queue()

    rect[0][0] = 1
    qu.put([0, 0])

    while (not qu.empty()):
        arr = qu.get()

        elex = arr[0]
        eley = arr[1]

        if elex > 0 and eley > 0 and rect[elex - 1][eley - 1] == 0:
            rect[elex - 1][eley - 1] = 1
            v = [elex - 1, eley - 1]
            qu.put(v)

        if elex > 0 and rect[elex -1][eley] == 0:
            rect[elex - 1][eley] = 1
            v = [elex -1, eley]
            qu.put(v)

        if elex > 0 and eley < n -1 and rect[elex -1][eley + 1] == 0:
            rect[elex - 1][eley + 1] = 1
            v = [elex - 1, eley + 1]
            qu.put(v)

        if eley > 0 and rect[elex][eley -1] == 0:
            rect[elex][eley - 1] = 1
            v = [elex, eley - 1]
            qu.put(v)

        if eley < n -1 and rect[elex][eley + 1] == 0:
            rect[elex][eley + 1] = 1
            v = [elex, eley + 1]
            qu.put(v)

        if elex < m - 1 and eley > 0 and rect[elex + 1][eley - 1] == 0:
            rect[elex + 1][eley - 1] = 1
            v = [elex + 1, eley - 1]
            qu.put(v)

        if elex < m - 1 and rect[elex + 1][eley] == 0:
            rect[elex + 1][eley] = 1
            v = [elex + 1, eley]
            qu.put(v)

        if elex < m -1 and eley < n - 1 and rect[elex + 1][eley + 1] == 0:
            rect[elex + 1][eley + 1] = 1
            v = [elex + 1, eley + 1]
            qu.put(v)

    return rect[m - 1][n - 1] == 1

m1 = 5
n1 = 5
k1 = 2
r1 = 1
X1 = [1, 3]
Y1 = [3, 3]

# Function call
if (is_possible(m1, n1, k1, r1, X1, Y1)):
    print("Possible")
else:
    print("Not Possible")

# Test case 2
m2 = 5
n2 = 5
k2 = 2
r2 = 1
X2 = [1, 1]
Y2 = [2, 3]

# Function call
if (is_possible(m2, n2, k2, r2, X2, Y2)):
    print("Possible")
else:
    print("Not Possible")
