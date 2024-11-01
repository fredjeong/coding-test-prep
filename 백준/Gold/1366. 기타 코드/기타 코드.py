import sys
input = sys.stdin.readline

n, m = map(int, input().split()) # n: 기타의 줄의 개수, m: 코드를 구성하는 음의 개수
base = input().split()
chord = input().split()

arr = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]

for i in range(n):
    base[i] = arr.index(base[i])

for i in range(m):
    chord[i] = arr.index(chord[i])


visited = [False for _ in range(m)]
fret = [0 for _ in range(n)]

s = set()
def dfs(base_, fret_, visited_, idx):
    if idx == len(base_):
        if False in visited_:
            return
        new_fret = [fret_[i] for i in range(len(fret_)) if fret_[i] > 0]
        if new_fret:
            if new_fret:
                s.add(max(new_fret) - min(new_fret) + 1)

        else:
            s.add(0)
        return

    # 모든 코드에 집어넣어보기
    for i in range(m):
        base = base_[:]
        fret = fret_[:]
        visited = visited_[:]
        visited[i] = True

        fret[idx] = chord[i] - base[idx]
        if fret[idx] < 0:
            fret[idx] += 12

        dfs(base, fret, visited, idx+1)
        fret[idx] += 12
        dfs(base, fret, visited, idx+1)

dfs(base, fret, visited, 0)
print(min(s))