import heapq

T = int(input())

for test_case in range(1, T+1):
    k = int(input())
    string = input().strip() # 길이 최대 400
    # 사전적 순서로 k번째에 해당하는 접미어를 찾아 출력하기
    q = []
    substring = ""
    for i in range(1, len(string)+1):
        substring = string[-i] + substring
        q.append(substring)
    heapq.heapify(q)

    if len(q) < k :
        answer = "none"
    else:
        answer = heapq.nsmallest(k, q)[-1]
    print(f"#{test_case} {answer}")
