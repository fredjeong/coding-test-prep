def solution(str_list):
    answer = []
    if "l" in str_list and "r" in str_list:
        index = min(str_list.index("l"), str_list.index("r"))
        if index == str_list.index("l"):
            if index != 0:
                answer = str_list[:index]
        else:
            if index != len(str_list) - 1:
                answer = str_list[index+1:]
    elif "l" in str_list and "r" not in str_list:
        index = str_list.index("l")
        if index != 0:
            answer = str_list[:index]
    elif "l" not in str_list and "r" in str_list:
        index = str_list.index("r")
        if index != len(str_list) - 1:
            answer = str_list[index+1:]
        
        
#            
#    for i in range(len(str_list)):
#        if str_list[i] == "l":
#            if i != 0:
#                for j in range(i):
#                    answer.append(str_list[j])
#            break
#        elif str_list[i] == "r":
#            if i != len(str_list - 1):
#                for j in range(i):
#                    answer.append(str_list[i + j])
#            break
    return answer