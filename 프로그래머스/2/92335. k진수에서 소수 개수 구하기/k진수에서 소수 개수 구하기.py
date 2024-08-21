def solution(n, k):
    answer = 0
    num = convert(n,k)
    nums = str(num).split("0")
    for x in nums:
    	#x가 비어있는 경우를 예외처리 한다
        if x and isPrime(int(x)):
            answer += 1
    return answer

def convert(n,k):
    if k == 10:
        return n
    else:
        new_n = ""
        while n > 0:
            new_n += str(n % k)
            n = n // k
        return new_n[::-1]

def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**(1/2)+1)):
        if n % i == 0:
            return False
    return True
    

#def solution(n, k):
#    answer = 0
#    
#    # n을 k진수로 변환
#    n_converted = convert(n,k)
#    # 에라토스테네스의 체
#    prime_list = prime(int(n_converted))
#    
#    # 0을 기준으로 split해서 배열 만들기
#    n_converted = n_converted.split("0")
#
#    # 배열의 수들을 딕셔너리로 변환
#    dic = {}
#    for i in n_converted:
#        if i.isdigit():
#            if i not in dic:
#                dic[i] = 1
#            else:
#                dic[i] += 1
#    
#    # 딕셔너리의 키들을 리스트로 반환
#    keys = list(dic.keys())
#    
#    # 주어진 수가 소수라면 딕셔너리에서 그 키의 밸류를 answer에 추가
#    for i in range(len(keys)):
#        if int(keys[i]) in prime_list:
#            answer += dic[keys[i]]
#            
#    return answer
#
#def convert(n, k):
#    converted = ""
#    power = 0
#    while n != 0:
#        power += 1
#        converted += str((n % (k ** power)) // (k ** (power - 1)))
#        n -= (n % (k ** power))
#    converted = converted[::-1]
#    return converted
#
#def prime(n):
#    arr1 = [True for _ in range(n+1)]
#    for i in range(2, int(n**0.5 + 1)):
#        if arr1[i] == True:
#            j = 2
#            while i * j <= n:
#                arr1[i * j] = False
#                j += 1
#    arr2 = []
#    for i in range(2, n + 1):
#        if arr1[i]:
#            arr2.append(i)
#    return arr2