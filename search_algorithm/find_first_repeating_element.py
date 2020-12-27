"""
Cho một dãy số, tìm phần tử lặp lại mà xuất hiện sớm nhất trong dãy?
Scan từ phải qua trái, cập nhật minimun index khi mà phần tử hiện tại đã được duyệt qua
"""

def printFirstRepeating(arr, n):
    min_index = -1
    
    myset = dict()

    for i in range(len(arr)-1, -1, -1):
        if arr[i] in myset:
            min_index = i
        else:
            myset[arr[i]] = 1

    return min_index



# Driver Code 
arr = [10, 5, 3, 4, 3, 5, 6] 
  
n = len(arr) 
print(printFirstRepeating(arr, n))
