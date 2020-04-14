import sys
from collections import deque

sys.setrecursionlimit(10000)


# leaf node count
def dfs(node):
    global parent, N, M, root, ans

    # 만약 지울 노드라면
    if node == M:
        return 0

    # 자식수가 없으면 리프노드이다
    if child[node] == 0:
        ans += 1
        return

    # loop 돌면서 자식노드가 있는 노드를 dfs로 탐색
    for c in range(N):
        # 현재 node를 부모로 가지는 자식노드를 찾아서 dfs 탐색
        if parent[c] == node:
            dfs(c)


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    child = [0 for _ in range(52)]
    ans = 0

    # i번쨰 노드의 부모노드를 입력받음
    parent = list(map(int, sys.stdin.readline().split()))
    # i번쨰 노드의 자식노드수를 저장
    for i, node in enumerate(parent):
        if node == -1:
            root = i
        else:
            child[node] += 1  # 자식노드수 증가
    # 지울노드 입력받으면 지울노드의 부모노드 자식수 감소
    M = int(sys.stdin.readline())
    child[parent[M]] -= 1

    # print(parent)
    # print(child)
    if M == root:
        print(0)
    else:
        dfs(root)
        print(ans)
