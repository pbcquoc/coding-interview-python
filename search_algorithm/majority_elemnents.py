"""
cho dãy số có kích thước là n, tìm phần tử xuất hiện nhiều hơn n//3 lần, 
Cách 1:
    Boyer-Moore-Majority-Vote-algorithm
    ý tưởng là nểu phần tử đó là majority thì khi cancel những phần tử khác thì sẽ còn lại chính nó 
"""
def bm(nums):
    count1, count2, cand1, cand2 = 0, 0, None, None
    for n in nums:
        if n == cand1:
            count1 += 1
        elif n == cand2:
            count2 += 1
        elif count1 == 0:
            cand1 = n
            count1 = 1
        elif count2 == 0:
            cand2 = n
            count2 = 1
        else:
            count1 -= 1
            count2 -= 1
                
    return [x for x in (cand1, cand2) if nums.count(x) > len(nums)//3]

arr = [3,2,3]
print(bm(arr))
