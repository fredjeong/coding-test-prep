def solution(data, ext, val_ext, sort_by):
    data_info = ["code", "date", "maximum", "remain"]
    index_criterion = data_info.index(ext)
    index_sort = data_info.index(sort_by)
    answer = []
    for i in range(len(data)):
        # data에서 ext 값이 val_ext보다 작은 데이터를 뽑는다
        if data[i][index_criterion] < val_ext:
            answer.append(data[i])
    # sort_by에 해당하는 값을 기준으로 오름차순으로 정렬한다
    answer.sort(key=lambda x : x[index_sort])
    return answer