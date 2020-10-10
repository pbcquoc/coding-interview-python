"""
Given a sorted array arr[] of size n and an element x to be searched in it. Return index of x if it is present in array else return -1.

Fibonacci Search divides given array in unequal parts
Binary Search uses division operator to divide range. Fibonacci Search doesn’t use /, but uses + and -. The division operator may be costly on some CPUs.
Fibonacci Search examines relatively closer elements in subsequent steps. So when input array is big that cannot fit in CPU cache or even in RAM, Fibonacci Search can be useful.
"""

def fibonaccian_search(arr, x, n):
    fib2 = 0
    fib1 = 1
    fib0 = fib1 + fib2
    while fib0 < n:
        fib2 = fib1 
        fib1 = fib0
        fib0 = fib1 + fib2
    
    offset = -1
    while fib0 > 1:
        i = min(offset + fib2, n - 1)
        if (x > arr[i]):
            fib0 = fib1
            fib1 = fib2
            fib2 = fib0 - fib1
            offset = i
        elif (x < arr[i]):
            fib0 = fib2
            fib1 = fib1 - fib2
            fib2 = fib0 - fib1
        else:
            return i
    
    if arr[offset + 1]== x:
        return offset + 1

    return -1
# Driver Code 
arr = [10] 
n = len(arr) 
x = 10
print("Found at index:", fibonaccian_search(arr, x, n)) 
