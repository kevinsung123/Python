from collections import deque


def solution(n, results):
    answer = 0
    adj = [[] for i in range(n + 1)]
    indgree = [0 for i in range(n + 1)]
    for i in results:
        src, dest = i
        adj[src].append(dest)
        indgree[dest] += 1
    q = deque()
    print(adj)
    # 정렬시작
    for i in range(n + 2):
        if indgree[i+1] == 0:
            q.append(i+1)
    ans = []
    road = [0 for i in range(n+1)]
    print(q)
    for i in range(n + 1):
        if len(q) == 0:
            answer = 0
            break
        cur = q.popleft()
        road[i] = cur + 1
        for i in adj[cur]:
            if --indgree[i] == 0:
                q.append(i)
    print(road)
    return answer


if __name__ == '__main__':
    results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
    n = 5
    solution(n, results)
