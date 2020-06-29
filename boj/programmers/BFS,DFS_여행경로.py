from collections import deque,defaultdict
from heapq import *



def solution(tickets):
    answer = []
    routes = defaultdict(list)

    for start, end in tickets:
        routes[start].append(end)
    # 2. 시작점 - [끝점] 역순으로 정렬
    print(routes)

    return answer


if __name__ == '__main__':
    # tickets=[['ICN', 'JFK'], ['HND', 'IAD'], ['JFK', 'HND']]
    tickets = [['ICN', 'SFO'], ['ICN', 'ATL'], ['SFO', 'ATL'], ['ATL', 'ICN'], ['ATL', 'SFO']]
    solution(tickets)
