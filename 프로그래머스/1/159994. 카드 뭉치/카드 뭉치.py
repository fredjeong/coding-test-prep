def solution(cards1, cards2, goal):
    answer = "Yes"
    
    while goal:
        if len(goal) == 0:
            answer = "Yes"
            break
        else:
            if len(cards1) != 0 and goal[0] == cards1[0]:
                goal.remove(goal[0])
                cards1.remove(cards1[0])
            elif len(cards2) != 0 and goal[0] == cards2[0]:
                goal.remove(goal[0])
                cards2.remove(cards2[0])
            else:
                answer = "No"
                break
    return answer