import sys


def solve():
    global S
    S = list(S)
    ans = []
    while len(S) > 0:
        print(''.join(S))
        ans.append(''.join(S))
        S.pop(0)
    ans.sort()

    for i in ans:
        pass
       # print(i)


if __name__ == '__main__':
    S = sys.stdin.readline()
    solve()
