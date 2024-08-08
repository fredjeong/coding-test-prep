def solution(lottos, win_nums):
    count = 0
    zeros = 0
    for i in lottos:
        if i in win_nums:
            count += 1
        elif i == 0:
            zeros += 1
    
    best = count + zeros
    if best >= 2:
        best_rank = 7 - best
    else:
        best_rank = 6
        
    worst = count
    if worst >= 2 :
        worst_rank = 7 - worst
    else:
        worst_rank = 6
    
    answer = [best_rank, worst_rank]

    return answer