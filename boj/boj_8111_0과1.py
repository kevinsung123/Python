import sys
from collections import deque


# N의 나머지는 0-N-1
# visited 배열에 나머지들의 방문여부 체크
# 이미 들어있으면 넘어가고 안들어있으면 추가
# 나머지가 0이면 이값은 n의배수이면서 조건을 만족 최소의 수
#

def bfs(n):


    # 나머지 방문여부 확인
    visited = [ -1 for _ in range(n)]
    # 트리 역추적 배열
    parent =[0 for _ in range(n)]
    # 0또는 1 어떤수인지
    pc = [0 for _ in range(n)]

    # 탐색 시작 1부터 시작
    q = deque()
    q.append(1)
    visited[1] = 1
    # 루트
    parent[1] = -1

    while len(q) > 0:
        cur = q.popleft()
        # 0또는 1을 붙여가면서 체크
        for k in range(2):
            next = (cur * 10 + k) % n
            #print("cur=",cur)
            #print("next=",next)
            # 방문하지 않았다면
            if visited[next] == -1:
                parent[next] = cur
                # 문자열 저장
                pc[next] = k
                # 방문체크
                visited[next] = 1
                q.append(next)
    print(parent)
    print(visited)
    print(pc)
    if visited[0] == -1:
        print("BRAK")
    else :
        cur=0
        ans=''
        while parent[cur]!=-1:
            ans+=str(pc[cur])
            cur=parent[cur]
        print(ans.reverse())




if __name__ == '__main__':

    T = int(input())
    test_case = []
    for _ in range(T):
        bfs(int(input()))
