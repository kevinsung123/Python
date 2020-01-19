### 힙자료구조
- 모듈 import : import heapq or from heapq import *
- 최소 힙 생성
	- heapq모듈 호출때 마다 리스트를 인자로넘겨한다
	- heapq모듈을 통해서 원소를 추가하거나 삭제한 리스트가 그냥 최소힙
	```
	from heapq import *  
	import sys
		q = []  
		heappush(q, (0, 1, k))
		d, cur, cnt = heappop(q)  # d=거리 cur=현재 정점 cnt=도로 포장 가능 횟수
		heapq.heappop(q)
		q[0] #삭제하지않고 원소조회
	```
- 기존리스트를 힙으로 변환
	- heapq모듈의 heapfiy()함수이용
	```
	heap=[4,1,7,3,8,5]
	heapq.heapify(heap)
	print(heap)
	```
- 최대힙
	- 기본적으로 최소힙(오름차순)
	- 힙에 튜플을 원소로 추가허간 삭제하면 튜플내에서 맨앞에 있는 값을 기준으로 최소힙이 구성되는 원리 이용
	- (우선순위,값) 구조의 튜플을 힙에 추가하거나/삭제
	- 값을 읽어올때는 각 튜플에서 인덱스1에 있는값을 취하면 된다
### 예제
```
from heapq import *  
num = [4, 1, 7, 3, 8, 5]  
q = []  
# max heap  
print("===========maxheap===========")  
for n in num:  
    heappush(q, (-n, n))  # 우선순위와 값을 값이넣는다  
print("n번쨰 값을 구할때")  
print(nlargest(2, q))  
while q:  
    print(heappop(q)[1])  
  
# main heap  
print("==========minheap===========")  
minq = []  
for n in num:  
    heappush(minq, n)  
print("The 3 largest numbers in list are : ", end="")  
print(nlargest(3, minq))  
print("The 3 smallest numbers in list are : ", end="")  
print(nsmallest(3, minq))  
  
while minq:  
    print(heappop(minq))  
  
print("정렬 ", end=" ")  
arr = [9, 1, 6, 4, 2, 8, 3, 7, 5]  
print(sorted(arr))  
print(sorted(arr,reverse=True)[:3])  
print("n번쨰 정렬 ", end=" ")  
print(sorted(arr)[0:3]) # 0<= <3
```
