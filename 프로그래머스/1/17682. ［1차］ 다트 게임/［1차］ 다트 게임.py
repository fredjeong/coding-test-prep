def solution(dartResult):
    arr = []
    for i in range(0, len(dartResult)):
        if dartResult[i].isdigit():
            if dartResult[i] == "0":
                if i == 0:
                    arr.append(dartResult[i])
                else:
                    if not dartResult[i-1].isdigit():
                        arr.append(dartResult[i])
            else: 
                if dartResult[i+1].isdigit():
                    arr.append(dartResult[i:i+2])
                else:
                    arr.append(dartResult[i])
        elif dartResult[i] == "S" or dartResult[i] == "D" or dartResult[i] == "T":
            arr.append(dartResult[i])
        elif dartResult[i] == "*" or dartResult[i] == "#":
            arr.append(dartResult[i])

    score = []
    bonus = []
    option = []
    for i in range(len(arr)):
        if arr[i].isdigit():
            if i == 0:
                score.append(arr[i])
            else:
                if arr[i-2].isdigit():
                    option.append(" ")
                    score.append(arr[i])
                else:
                    score.append(arr[i])
        elif arr[i].isalpha():
            if i == len(arr)-1:
                bonus.append(arr[i])
                option.append(" ")
            else:
                bonus.append(arr[i])
        else:
            option.append(arr[i])

    for i in range(len(bonus)):
        if bonus[i] == "S":
            bonus[i] = 1
        elif bonus[i] == "D":
            bonus[i] = 2
        else:
            bonus[i] = 3

    results = []
    for i in range(3):
        temp_score = int(score[i])
        temp_bonus = bonus[i]
        temp_option = option[i]
        temp = temp_score ** temp_bonus
        if temp_option == "#":
            temp *= (-1)
        elif temp_option == "*":
            if i == 0:
                temp *= 2
            else:
                temp *= 2
                results[i-1] *= 2
        results.append(temp)

    answer = sum(results)
    return answer