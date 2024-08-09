def solution(numbers, hand):
    left = [1, 4, 7]
    right = [3, 6, 9]
    dic = {1: [0,0], 2: [0,1], 3: [0,2], 4: [1,0], 5: [1,1], 6: [1,2], 
           7: [2,0], 8: [2,1], 9: [2,2], 0: [3,1]}
    left_position = [3,0]
    right_position = [3,2]
    answer = ''
    for i in numbers:
        if i in left:
            answer += "L"
            left_position = dic[i]
        elif i in right:
            answer += "R"
            right_position = dic[i]
        else:
            left_distance = abs(left_position[0] - dic[i][0]) + abs(left_position[1] - dic[i][1])
            right_distance = abs(right_position[0] - dic[i][0]) + abs(right_position[1] - dic[i][1])
            if hand == "left":
                if left_distance <= right_distance:
                    answer += "L"
                    left_position = dic[i]
                else:
                    answer += "R"
                    right_position = dic[i]
            else:
                if left_distance < right_distance:
                    answer += "L"
                    left_position = dic[i]
                else:
                    answer += "R"
                    right_position = dic[i]
    return answer