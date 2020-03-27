#### Python Queue구현 방법
1. **list**
- list는 Python의 기본 자료구조
- append : enQueue 
- pop : deQueue
- insert/delete를 처리하기에는 느리다  O(n) 소요
```
#initialize queue
queue=[]

#adding elements 
queue.append('a')
queue.append('b')
queue.append('c')
print(queue)
=> a b c
#removing elements
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))
=> a b c 
```
2. **collection.deque**
- dequeue 클래스를 활용
- from collection module에 존재
- O(1) 소요
```
from collection import deque

# initialize queue
q = deque() 

# adding elements
q.append('a')
q.append('b')
q.append('c')

# removing elements
q.popleft()
q.popleft()
q.popleft()


```
4. **queue.Queue**
- Python의 built-in 모듈
-  queue.Queue(maxsize) 
- maxsize=0이면 무한대 queue의미
- 메소드
	- maxsize : queue에서 허용된 max element개수 
	- empty() : T/F=> queue가 empty 여부
	- full() : T/F =>queue에서 maxsize item여부  
	- get() : queue에서 element를 제거하고 맨앞의 item을 리턴
	- put() : queue에 itme를 삽입
	- qsize() : 현재 queue의 size를 리턴
```
rom queue import Queue 
  
# Initializing a queue 
q = Queue(maxsize = 3) 
  
# qsize() give the maxsize  
# of the Queue  
print(q.qsize())  
  
# Adding of element to queue 
q.put('a') 
q.put('b') 
q.put('c') 
  
# Return Boolean for Full  
# Queue  
print("\nFull: ", q.full())  
  
# Removing element from queue 
print("\nElements dequeued from the queue") 
print(q.get()) 
print(q.get()) 
print(q.get()) 
  
# Return Boolean for Empty  
# Queue  
print("\nEmpty: ", q.empty()) 
  
q.put(1) 
print("\nEmpty: ", q.empty())  
print("Full: ", q.full()) 
  
# This would result into Infinite  
# Loop as the Queue is empty.  
# print(q.get()) 
```
