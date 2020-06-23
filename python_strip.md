### Strip
- 설명 
	- python built-in 함수
	- leading, trailing character들을 제거한 string의 copy본을 return
- synatx
	- parameter
		- 제거할 string을 함수 입력값으로 넣는다
		-  아무것도 넣지 않으면 default로 앞/뒤 공백제거
- 빈칸이 없는 문자열을 입력받고 list로 저장할떄
```
N, K = map(int, sys.stdin.readline().split())  
left=list(sys.stdin.readline().strip())  # strip으로 마지막 \n 제거
right=list(sys.stdin.readline().strip())
```
