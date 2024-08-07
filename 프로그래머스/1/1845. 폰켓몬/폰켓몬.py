def solution(nums):
    unique = []
    for i in nums:
        if i not in unique:
            unique.append(i)
    unique = len(unique)
    
    n = len(nums)
    k = n//2
    
    if unique > k:
        answer = k
    else:
        answer = unique
    
    return answer