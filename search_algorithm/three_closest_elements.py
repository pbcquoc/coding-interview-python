"""
cho 3 dãy số đã được sắp sếp A, B, C, tìm kiếm 3 phần tử i, j, k, mỗi phần tử từ mỗi dãy số, sao cho max(abs(A[i]-B[j]), abs(B[j]-C[k]), abs(C[k]-A[i])) nhỏ nhất 
Solution:
    max(abs(A[i]-B[j]), abs(B[j]-C[k]), abs(C[k]-A[i])) chính là khoảng cách giữa phần tử nhỏ nhất và lớn nhất. 
"""
def find_closest(A, B, C):
    diff = 9999
    rs_i, rs_j, rs_k = 0, 0, 0
    i, j, k = 0, 0, 0 

    while (i < len(A) and j < len(B) and k < len(C)):
        minimum = min(A[i], min(B[j], C[k]))
        maximum = max(A[i], max(B[j], C[k]))
        
        if maximum - minimum < diff:
            diff = maximum - minimum
            rs_i, rs_j, rs_k = i, j, k

        if diff == 0:
            break

        if A[i] == minimum:
            i += 1
        elif B[j] == minimum:
            j += 1
        else:
            k += 1

    return A[rs_i], B[rs_j], C[rs_k]

A = [1, 4, 10]
B = [2, 15, 20]
C = [10, 12]

rs = find_closest(A,B,C)
print(rs)

