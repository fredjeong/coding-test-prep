def solution(id_list, report, k):
    reported_count = {user: 0 for user in id_list} # 피신고자 신고당한 횟수 보관
    report_dic = {user: [] for user in id_list} # 신고자-피신고자 쌍 보관
    
    for i in range(len(report)):
        temp = report[i].split(" ")
        if temp[1] not in report_dic[temp[0]]:
            report_dic[temp[0]].append(temp[1]) # 신고자-피신고자 쌍 추가
            reported_count[temp[1]] += 1 # 피신고자 신고횟수 추가
    
    email_dic = {user: 0 for user in id_list}
    
    for i in id_list:
        if reported_count[i] >= k:
            for j in id_list:
                if i in report_dic[j]:
                    email_dic[j] += 1
    
    answer = list(email_dic.values())

    return answer