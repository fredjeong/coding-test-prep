import sys

input = sys.stdin.readline

while True:
    line = input().strip()
    if line == "0":
        break
    else:
        if len(line) == 1:
            print("yes")
            continue

        is_break = False
        for i in range(len(line)//2):
            if line[i] != line[-1-i]:
                print("no")
                is_break = True
                break
        if is_break == False:
            print("yes")