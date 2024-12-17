import sys
from itertools import permutations

input = sys.stdin.readline

t = int(input()) # 테스트 데이터의 개수

def solution(pref):
    match = {}
    girl_idx = {}

    for person in range(1, 11):
        match[person] = 11

        if person >= 6:
            girl_idx[person] = 0

    while 11 in match.values():
        for girl in range(6, 11):
            # 퇴짜를 받은 여학생들만 다음 라운드에 다시 참여한다.
            if match[girl] != 11:
                continue

            # 6번 여학생부터 선호도 리스트를 보면서 가장 좋아하는 남학생에게 프러포즈를 한다.
            boy = pref[girl][girl_idx[girl]]

            # 남학생이 짝이 없는 경우 무조건 프러포즈를 받아들인다
            if match[boy] == 11:
                match[boy] = girl
                match[girl] = boy

            # 남학생이 짝이 있는 경우 두 명에 대한 자신의 선호도를 비교해서 더 좋아하는 여학생과 잠정적으로 짝이 되고 다른 여학생에게는 퇴짜를 놓게 된다.
            else:
                prev_girl = match[boy]
                prev_girl_pref = pref[boy].index(prev_girl)
                girl_pref = pref[boy].index(girl)

                if prev_girl_pref < girl_pref:
                    girl_idx[girl] += 1
                else:
                    match[prev_girl] = 11
                    girl_idx[prev_girl] += 1

                    match[girl] = boy
                    match[boy] = girl

    return match[1]


for _ in range(t):
    pref = {}
    pref[1] = [6, 7, 8, 9, 10]

    for person in range(2, 11):
        pref[person] = list(map(int, input().split())) # 선호도 반영

    # 원래 선호도에서 태현이의 짝
    threshold = solution(pref)

    if threshold == 6:
        print("NO")
    else:
        early_stopping = False
        for case in permutations([6, 7, 8, 9, 10]):
            pref[1] = list(case)

            result = solution(pref)
            if result < threshold:
                print("YES")
                early_stopping = True
                break

        if not early_stopping:
            print("NO")