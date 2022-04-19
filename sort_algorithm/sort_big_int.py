"""
https://www.geeksforgeeks.org/sorting-big-integers/
* if the lengths are different, just compare length
* if the lengths are same, compare lexicon 
"""
def sort_big_int(arr, n):
    arr.sort(key=lambda x: (len(x), x))

arr = ["54", "724523015759812365462", "870112101220845", "8723"]
sort_big_int(arr, len(arr))
print(arr)
