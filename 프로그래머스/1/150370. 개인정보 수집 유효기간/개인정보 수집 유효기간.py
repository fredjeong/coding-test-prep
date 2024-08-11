def solution(today, terms, privacies):
    answer = []
    term_dic = {}
    for term in terms:
        temp = term.split(" ")
        term_dic[temp[0]] =int(temp[1]) * 28
    
    today = today.split(".")
    today_year = int(today[0])
    today_month = int(today[1])
    today_day = int(today[2])
    
    for i in range(len(privacies)):
        term = privacies[i][-1]
        date = privacies[i][:-2].split(".")
        year = int(date[0])
        month = int(date[1])
        day = int(date[2])
        
        days_passed = (today_year - year) * 336 + (today_month - month) * 28 + (today_day - day) 
        if days_passed >= term_dic[term]:
            answer.append(i + 1)

    return answer