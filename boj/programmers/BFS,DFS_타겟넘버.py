from itertools import combinations, permutations,product
from sys import stdin

# 1번쨰 방법 비트마스킹 이용
def solution(numbers, target):
    answer = 0
    m = len(numbers)
        # bit 연산자 2^m의 경우수
    for bm in range(1 << m):
        sum = 0
        # 한가지 경우의 수가 정해짐
        for j in range(len(numbers)):
            # 1이면 +
            if bm & (1 << j):
                sum += numbers[j]
            # 0이면 -
            else:
                sum -= numbers[j]

        if sum == target:
            answer += 1
    return answer

# 2번쨰 


if __name__ == '__main__':
    numbers = [1, 1, 1, 1, 1]
    target = 3
    solution(numbers, target)
