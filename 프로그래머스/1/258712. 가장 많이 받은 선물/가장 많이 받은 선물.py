def solution(friends, gifts):
    # 선물 지수 딕셔너리로 보관: 친구들에게 준 선물의 수에서 받은 선물의 수를 뺀 값
    gift_index = {friend: 0 for friend in friends}
    
    # 개인이 누구에게 선물을 줬는지 그 횟수와 함께 딕셔너리에 보관
    gift_list = {giver: {} for giver in friends}
    for giver in friends:
        for receiver in friends:
            if giver != receiver:
                gift_list[giver][receiver] = 0
    
    for gift in gifts:
        temp = gift.split(" ")
        giver = temp[0]
        receiver = temp[1]
        gift_index[giver] += 1
        gift_index[receiver] -= 1
        gift_list[giver][receiver] += 1

    next_month = {friend: 0 for friend in friends}
    
    # 선물 받을 횟수 카운트
    for giver in friends:
        for receiver in friends:
            if giver != receiver:
                # 두 사람이 선물을 주고받은 기록이 있다면
                if gift_list[giver][receiver] != gift_list[receiver][giver]:
                    if gift_list[giver][receiver] > gift_list[receiver][giver]:
                        next_month[giver] += 1
                # 두 사람이 선물을 주고받은 기록이 하나도 없거나 주고받은 횟수가 같다면
                else:
                    if gift_index[giver] > gift_index[receiver]:
                        next_month[giver] += 1
    
    answer = max(next_month.values())
    return answer