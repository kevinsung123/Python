# Python : sys.stdin.readline() vs input() 차이점
* 입출력 스트림에 대한 문제 같습니다.
* 파이썬이 동적변수라지만 변수의 형태로 저장하기 위해서 input() 메소드 내에서 가공을 할텐데
* raw_input() 은 문자열을 반환하고 input() 은 raw_input() 을 evaluate한 결과를 반환합니다.
* sys.stdin.readline() 은 한 줄의 문자열를 반환하는데 이것을 int() 로 묶어서 정수로 변환하는게 더 빠른가봅니다.
* 다른 언어에도 똑같은 원리가 적용되지요.
* Java에서는 Scanner 보다 Buffered~ 가 더 처리가 가볍고, C++에서는 cout 보다 printf 를 이용하는게 시간적인 측면에서 효율적이라고 알고있습니다.
* C++은 함수오버로딩도 있고 해서 훨씬 오래 걸리는것 같지만요..

# Python : 이차원리스트로 문자열 입력받기

* 한칸씩 공백으로 이차원 문자열이 들어올경우 
	> a b c d 
	<br>
	> e f g h
	>=> board = [list(sys.stdin.readline().split()) for _ in range(R)]
* 공백없이 문자열이 들어올경우
	> a b c d 
	<br>
	> e f g h
	>=> board = [list(sys.stdin.readline().strip()) for _ in range(R)]
* 이차원리스트 초기화 
	> cache = [['' for _ in range(C)] for _ in range(R)]
	
# Python : eval() 함수 
[참조](https://bluese05.tistory.com/64)