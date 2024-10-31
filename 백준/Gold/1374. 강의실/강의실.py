import sys
input = sys.stdin.readline

import heapq

class Problem():
    def __init__(self):
        self.n = int(input())
        self.lectures = []
        for _ in range(self.n):
            lecture_num, start_time, end_time = map(int, input().split())
            self.lectures.append([start_time, end_time])
        self.lectures.sort()

    def run(self):
        schedule = []
        heapq.heapify(schedule)

        for start_time, end_time in self.lectures:
            if not schedule:
                heapq.heappush(schedule, end_time)
                continue
            min_start_time = heapq.heappop(schedule)
            if start_time < min_start_time:
                heapq.heappush(schedule, end_time)
                heapq.heappush(schedule, min_start_time)
                continue
            else:
                heapq.heappush(schedule, end_time)
        print(len(schedule))

def main():
    instance = Problem()
    instance.run()

if __name__ == "__main__":
    main()