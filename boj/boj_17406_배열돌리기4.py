import sys
from itertools import permutations

if __name__ == '__main__':
    N, M, K = map(int, sys.stdin.readline().split())
    arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    print(arr)
    rotate = [list(map(int, sys.stdin.readline().split())) for _ in range(K)]
    print(rotate)
