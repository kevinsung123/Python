import collections


dq = collections.deque([1, 2, 3])
# 맨 끝에 삽입
dq.append(4)
# 맨 앞에 삽입
dq.appendleft(0)
# 맨 뒤 삭제
dq.pop()
# 맨 앞 삭제
dq.popleft()
# 해당 원소의 위치를 반환
find = dq.index(3, 0, len(dq))
# 중간에 삽입
dq.insert(0, 10)
# 해당 수의 개수
c = dq.count(10)
print("count=", c)
print("find index=", find)
print(dq)
dq.rotate(1)
print(dq)
dq.rotate(-1)
print(dq)

