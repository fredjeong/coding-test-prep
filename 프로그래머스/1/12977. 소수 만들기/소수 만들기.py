def solution(nums):
    answer = 0
    # 우선 크기순으로 정렬
    nums = sorted(nums)
    for i in range(len(nums)):
        for j in range(1, len(nums)):
            for k in range(2, len(nums)):
                if i<j<k:
                    num = nums[i]+nums[j]+nums[k]
                    # 에라토스테네스의 체 이용하여 소수 만들어지는지 확인
                    arr = [l for l in range(2, int(num ** 0.5)+1)] # 2부터 num까지 들어있는 배열 생성
                    for divisor in arr:
                        if num % divisor == 0: # 소수 아님
                            break
                        else: 
                            if divisor == arr[-1]:
                                answer += 1

                    #if arr.count(True) == 3:
                    #    answer += 1

    return answer