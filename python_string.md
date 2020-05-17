#### 문자열 연산하기
#### 문자열 연결 concatenation
- 문자열 2개를 ```+``` 연산
```
>>> head = "Python"  
>>>> tail = " is fun!"  
>>>> head + tail 
'Python is fun!'
```
#### 문자열 곱하기
```
>>> a = "python"
>>> a * 2
'pythonpython
```
- ```*```의미는 반복의 의미 
#### 문자열 길이
- len(str): 문자열 길이

#### 문자열 인덱싱
- 인덱싱(indexing): 문자열 접근 혹은 가리킨다

```
>>> a = "Life is too short, You need Python"
Life is too short, You need Python
0         1         2         3 
0123456789012345678901234567890123

```
- 인덱싱은 0번쨰 인덱스부터 시작
- 인덱스 -1은 뒤에서부터 읽기 위함 뒤에서부터 세어 첫번째가 되는 문자 의미
#### 문자열 슬라이싱
- 슬라이싱(slicing) : 잘라낸다 
```
>>> a[0:2]
'Li'
>>> a[5:7]
'is'
>>> a[12:17]
'short'
```
- 문자열[시작번호 : 끝 번호] 를 하면 해당 부분 문자열 구함
- 끝번호 생략시 그 문자열의 끝까지 뽑아냄
```
>>> a[19:] 
'You need Python'
```
```
※ 문자열치환 
- 문자열은 immutable한 자료형이기떄문에 대입으로 변환할 할 수 없다
```
- reverse 문자열 방법
	1. 슬라이싱
	- 문자열[strlen : : -1]
	- 문자열[ : : -1]
	- 문자열[start : end : step]
		- step  양수일때 : 오른쪽으로 step만큼 이동하면서 가져옴
		- step 음수일때 : 왼쪽으로 step만큼 이동하면서 가져옴
	2. loop
	- 새로운 배열로 정의 reversedString[]
	```
	str="python"
	reversedString=[]
	index =len(str) 
	while index > 0 :
		reversedString+=str[index-1]
		index=index-1
	print(reversedString)
	``` 
  3. join
  - python의 iteratorl protocol을 사용하는방법
  - built-in 함수 reversed를 사용
  - reversed 결과값은 object이므로 join함수 이용하여 문자열 변환해줘야함
  ```
  str="Python"
  reversedStr=''.join(reversed(str
 ``
---
### 문자열 관련함수
- count : 문자열 세기  
```
>>> a = "hobby"
>>> a.count('b')
2
```
- find : 해당 문자의 위치 알려주기(찾는 문자나 문자열이 존재하지않으면 -1을반환)
- index: 해당 문자열 위치 처음찾은 위치반환(find와 다른점은 해당 문자 없을 시 에 오류)
```
>>> a = "Python is the best choice"
>>> a.find('b')
14
>>> a.find('k')
-1
```
- join : 문자열 삽입. 리스트나 튜플도 입력으로 사용 수 있음
```
>>> ",".join('abcd')
'a,b,c,d'
```
- upper : 소문자->대문자
- lower : 대문자->소문자
- lstrip : 왼쪽 공백 지우기
- rstrip : 오른쪽 공백 지우기
- strip : 양쪽 공백지우기
- replace : 문자열 바꾸기 
	- 문자열.replace("원본","타겟")
- split() : 문자열 나누기 
	- ```a.split()``` 과 같이 빈값이면 default로 공백(스페이스,탭,엔터)을 기준으로 문자열 나누어줌
	- ```a.split(":")``` 처럼 괄호 안에 특정 값이 있다면 그 값을 기준으로 문자열 나눔
```
>>> a = "Life is too short"
>>> a.split()
['Life', 'is', 'too', 'short']
>>> b = "a:b:c:d"
>>> b.split(':')
['a', 'b', 'c', 'd']
```

