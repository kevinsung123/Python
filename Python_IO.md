﻿## Python : sys.stdin.readline() vs input() 차이점  
* 입출력 스트림에 대한 문제 같습니다.  
* 파이썬이 동적변수라지만 변수의 형태로 저장하기 위해서 input() 메소드 내에서 가공을 할텐데  
* raw_input() 은 문자열을 반환하고 input() 은 raw_input() 을 evaluate한 결과를 반환합니다.  
* sys.stdin.readline() 은 한 줄의 문자열를 반환하는데 이것을 int() 로 묶어서 정수로 변환하는게 더 빠른가봅니다.  
* 다른 언어에도 똑같은 원리가 적용되지요.  
* Java에서는 Scanner 보다 Buffered~ 가 더 처리가 가볍고, C++에서는 cout 보다 printf 를 이용하는게 시간적인 측면에서 효율적이라고 알고있습니다.  
* C++은 함수오버로딩도 있고 해서 훨씬 오래 걸리는것 같지만요..  


  
## Python : 이차원리스트로 문자열 입력받기  
  
- 한칸씩 공백으로 이차원 문자열이 들어올경우  
```  
a b c d  
e f g h  
board = [list(sys.stdin.readline().split()) for _ in range(R)]  
```  
  
* 공백없이 문자열이 들어올경우  
```
abcd  
efgh  
board = [list(sys.stdin.readline().strip()) for _ in range(R)]  
 ```

* 이차원리스트 초기화  
``` 
cache = [['' for _ in range(C)] for _ in range(R)]  
```
- strip :
	- 양쪽문자를 제거 , 개행문자 제거
	-  strip(char) : char에해당하는 문자를 제거
  
## Python : eval() 함수  
[참조](https://bluese05.tistory.com/64)


## Python print
- python ""으로 둘러싸인 문자열은 + 연산과 동일
- 문자로 띄어쓰끼는 콤마로 처리
	```
	print("life","is","short")
	=>life is short
	``` 
- 한줄에 결과값 출력하기 
	- 매개변수 end를 사용(기본값은 개행)
	```
	for i in range(10):
		 print(i,end=' ')
	```
- sep 인자를 사용하면 콤마로 구분된 문자열을 다르게 결합할 수 있다(기본값은 공백)
- file인자를 사용하면 출력 결과를 파일, 표준에러러처리 가능
- format 방식
	 ```
	 print('나의 이름은 {}입니다'.format('한사람')) print('나의 이름은 "{0}"입니다. 나이는 {1}세이고 성별은 {2}입니다.'.format('한사람',33,'남성')) 
	 print('나이는 {1}세이고 성별은 {2}입니다. 나의 이름은 "{0}"입니다. '.format('한사람',33,'남성')) 
	 print('나이는 {age}세이고 성별은 {gender}입니다. 나의 이름은 "{name}"입니다. ' .format(name='한사람',age=33,gender='남성')) 
	 print('만세삼창 : {0}!!! {0}!!! {0}!!! '.format('만세')) print('삼삼칠 박수 : {0}!!! {0}!!! {1}!!! '.format('짝'*3,'짝'*7)) 
	 print('-' * 40)
	 ```