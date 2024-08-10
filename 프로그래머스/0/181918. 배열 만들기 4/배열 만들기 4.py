def solution(arr):
    i = 0
    stk = []
    while i < len(arr):
        if stk == []:
            stk.append(arr[i])
            i += 1
        else:
            if stk[-1] < arr[i]:
                stk.append(arr[i]) 
                i += 1
            else:
                stk = stk[:-1]
    return stk