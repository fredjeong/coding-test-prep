num = 10**6

num_list = [True for _ in range(num+1)]
num_list[0] = False
num_list[1] = False
for i in range(2, int(num**0.5)+1):
    for j in range(i*2, num+1, i):
        num_list[j] = False

ans_list = [i for i in range(num+1) if num_list[i]]
print(" ".join(map(str, ans_list)))