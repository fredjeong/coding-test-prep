def solution(files):
    answer = []
    arr = []
    
    for file in files:
        head = ""
        number = ""
        tail = ""
        index = 0
        # Head 분리
        for i in range(len(file)):
            if file[i].isdigit():
                break
            else:
                head += file[i]
                index += 1
        # index부터 보면서 number 분리
        for i in range(index, len(file)):
            if not file[i].isdigit():
                break
            else:
                number += file[i]
                index += 1
        # index부터 보면서 tail 분리
        for i in range(index, len(file)):
            tail += file[i]
        
        # head, number, tail 리스트에 추가
        arr.append([head, number, tail])
    
    arr = sorted(arr, key=lambda x: (x[0].lower(), int(x[1])))
    
    for i in arr:
        temp = i[0] + i[1] + i[2]
        answer.append(temp)

    return answer