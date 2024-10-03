import sys
import heapq

input = sys.stdin.readline

n = int(input()) # 도시의 개수
m = int(input()) # 버스의 개수

graph = [[] for _ in range(n+1)]

for _ in range(m):
    departure, arrival, cost = map(int, input().split())
    graph[departure].append([arrival, cost])

start, end = map(int, input().split())
costs = [1e9 for _ in range(n+1)]

q = []
costs[start] = 0
heapq.heappush(q, [0, start])

while q:
    cur_cost, cur_node = heapq.heappop(q)
    if costs[cur_node] < cur_cost:
        continue
    for next_node, next_cost in graph[cur_node]:
        cum_cost = cur_cost + next_cost
        if cum_cost >= costs[next_node]:
            continue
        costs[next_node] = cum_cost
        heapq.heappush(q, [cum_cost, next_node])

print(costs[end])