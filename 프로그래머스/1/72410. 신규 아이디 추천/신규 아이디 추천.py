def solution(new_id):
    # new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
    for i in new_id:
        if i.isalpha():
            new_id = new_id.replace(i, i.lower())
    
    # new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
    allowed = ["-", "_", "."]
    temp = new_id
    new_id = ''
    for i in temp:
        if i.isalpha() or i.isdigit() or i in allowed:
            new_id += i

    # new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
    temp = new_id
    new_id = new_id[0]

    for i in range(1, len(temp)):
        if temp[i] != '.' or temp[i-1] != '.':
            new_id += temp[i]
    
    # new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
    new_id = new_id.strip('.')
    
    # new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
    if new_id == '':
        new_id += 'a'
    
    # new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
    # 만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
    if len(new_id) >= 16:
        temp = new_id
        new_id = ''
        for i in range(15):
            new_id += temp[i]
    new_id = new_id.rstrip('.')
    
    # new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
    while len(new_id) <= 2:
        new_id += new_id[-1]
    
    return new_id