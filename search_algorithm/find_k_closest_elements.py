"""
Cho dãy đã sorted, số k và x, trả về k số gần với x nhất
Tìm crossover point bằng binary search, crossover point là vị trí mà tại đó phần tử phía trước nhỏ hơn và phía sau lớn hơn 
Từ điểm crossover lấy k phần tử nhỏ nhất về bên 2 đầu. 
"""

def binary_search(arr, x, l, r):
    m = (l+r)//2
    
    if l == r -1 and arr[l] <= arr[m] < arr[r]:
        return l
    
    if arr[m] <= x:            
        return binary_search(arr, x, m, r)
    else:
        return binary_search(arr, x, l, m)
    
    
def findClosestElements(arr, k, x):
    """
    :type arr: List[int]
    :type k: int
    :type x: int
    :rtype: List[int]
    """
    
    if x <= arr[0]: 
        return arr[:k]
    
    if x >= arr[-1]:
        return arr[-k:]
      
    l = binary_search(arr, x, 0, len(arr)-1)
    
    r = l + 1
    
    count = 0
    while count < k and l >= 0 and r < len(arr):
        if x - arr[l] <= arr[r] - x:
            l = l - 1                
        elif x -arr[l] > arr[r] - x:
            r = r + 1
            
        count = count + 1
   
    while count < k and l >= 0:
        l = l -1
        count += 1
        
    while count < k and r < len(arr):
        r = r + 1
        count += 1
        
    return arr[l+1:r]

arr =[12, 16, 22, 30, 35, 39, 42,45, 48, 50, 53, 55, 56] 
x = 35
k = 4

print(findClosestElements(arr, k, x))
