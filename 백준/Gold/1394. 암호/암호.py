import sys
input = sys.stdin.readline

class Problem():
    def __init__(self):
        self.arr = list(input().strip()) # 최대 100자
        self.password = input().strip() # 길이 최대 1,000,000
        self.count = 0

    def run(self):
        arr_length = len(self.arr)
        password_length = len(self.password)

        # 시간 초과가 발생하지 않도록 미리 각 글자의 인덱스를 딕셔너리에 저장해두자
        index_dic = {}
        for i in range(arr_length):
            index_dic[self.arr[i]] = i

        # self.password의 길이 전까지는 중복순열 공식을 이용해 횟수를 추가해준다
        for _ in range(1, password_length):
            self.count *= arr_length
            self.count %= 900528
            self.count += arr_length
            self.count %= 900528

        # 각 글자의 암호에서의 자릿수와 메모한 문자 집합 self.arr에서의 인덱스 두 가지가 필요하다
        cnt = 0
        remainder = arr_length % 900528
        for order in range(password_length):
            # 글자 찾기
            char = self.password[order]

            # 문자 집합에서의 인덱스 찾기
            idx = index_dic[char]

            cnt *= remainder
            cnt %= 900528

            cnt += idx
            cnt %= 900528

        self.count += cnt
        print((self.count+1) % 900528)

def main():
    instance = Problem()
    instance.run()

if __name__ == "__main__":
    main()