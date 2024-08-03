def solution(before, after):
    before_list = []
    for i in before:
        before_list.append(i)
    before_list.sort()
    
    after_list = []
    for j in after:
        after_list.append(j)
    after_list.sort()
    
    if before_list == after_list:
        answer = 1
    else:
        answer = 0
    return answer