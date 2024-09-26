import sys

input = sys.stdin.readline

for i in range(3):
    a = input().strip()
    if a.isdigit():
        start = int(a) + 3 - i
        break

if start%3==0 and start%5==0:
    print("FizzBuzz")
elif start%3==0 and start%5!=0:
    print("Fizz")
elif start%3!=0 and start%5==0:
    print("Buzz")
else:
    print(start)