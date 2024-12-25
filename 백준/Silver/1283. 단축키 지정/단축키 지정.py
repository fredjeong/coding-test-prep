import sys

input = sys.stdin.readline

n = int(input())

chars = set()
for _ in range(n):
    text = input().strip()

    # 단어의 첫 글자가 이미 단축키로 지정되었는지 살펴본다
    early_stopping = False

    # 각 단어의 첫 번째 글자 검사
    result = ""
    for i in range(len(text)):
        if i == 0:
            if text[i].upper() not in chars and text[i].lower() not in chars:
                if early_stopping:
                    result += text[i]
                else:
                    early_stopping = True
                    chars.add(text[i])
                    result += "[" + text[i] + "]"
            else:
                result += text[i]
        elif text[i-1] == " ":
            if text[i].upper() not in chars and text[i].lower() not in chars:
                if early_stopping:
                    result += text[i]
                else:
                    early_stopping = True
                    chars.add(text[i])
                    result += "[" + text[i] + "]"
            else:
                result += text[i]
        else:
            result += text[i]
    if early_stopping:
        print(result)

    # 나머지 글자 검사
    if not early_stopping:
        result = ""
        for i in range(len(text)):
            if text[i] == " ":
                result += text[i]
            else:
                if text[i].upper() not in chars and text[i].lower() not in chars:
                    if early_stopping:
                        result += text[i]
                    else:
                        early_stopping = True
                        chars.add(text[i])
                        result += "[" + text[i] + "]"
                else:
                    result += text[i]
        print(result)