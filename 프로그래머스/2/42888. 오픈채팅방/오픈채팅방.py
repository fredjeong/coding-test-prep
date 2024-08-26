def solution(record):
    # 최종적으로 보는 메시지 출력
    answer = []
    nicknames = {}
    inouts = []
    
    for info in record:
        info = info.split(" ")
        user_act = info[0] # Enter / Leave / Change
        user_id = info[1]
        if user_act == "Enter":
            user_nickname = info[2]
            nicknames[user_id] = user_nickname
            inouts.append([user_id, user_act])
        elif user_act == "Leave":
            inouts.append([user_id, user_act])
        elif user_act == "Change":
            user_nickname = info[2]
            nicknames[user_id] = user_nickname
    
    for i in inouts:
        if i[1] == "Enter":
            message = nicknames[i[0]] + "님이 들어왔습니다."
            answer.append(message)
        elif i[1] == "Leave":
            message = nicknames[i[0]] + "님이 나갔습니다."
            answer.append(message)
    
    return answer