def binary_search(arr, l, r, x):    
    while l <= r:
        mid = (l+r)//2
        if x > arr[mid]:
            l = mid + 1
        elif x < arr[mid]:
            r = mid - 1
        else:
            return mid
    return -1

# Driver Code 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binary_search(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print ("Element is present at index % d" % result) 
else: 
    print ("Element is not present in array") 
