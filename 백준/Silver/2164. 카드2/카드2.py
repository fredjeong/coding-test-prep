import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

deck = deque()
for i in range(1, N+1):
    deck.append(i)

while len(deck) > 1:
    # 제일 위에 있는 카드를 버린다
    deck.popleft()
    # 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다
    temp = deck.popleft()
    deck.append(temp)

print(deck[0])