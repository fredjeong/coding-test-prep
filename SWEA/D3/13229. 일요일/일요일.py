T = int(input())
arr = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]

for test_case in range(1, T+1):
    day = input().strip()
    day_idx = arr.index(day)

    print(f"#{test_case} {7 - day_idx}")