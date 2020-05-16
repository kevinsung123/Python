#### _longobject 구조체
- CPython 의 git repo :https://github.com/python/cpython
- 이 중 int 구현을 담당하는 소스코드는 3개로 이루어짐
- 이 중 하나인 ```int```형 오브젝트를 나타나내는 자료형은 longintrepr.h에 있는 ```struct _longobject```
##### 구조
	- ```PyObject_VAR_HEAD```는 오브젝트들의 첫머리에 공통적으로 들어갈 것들을 모아놓은 매크로, garbage collection을 위한 reference count변수와 ```int``` 타입 자체에 대한 정의를 가진 구조체에 대한 포인터 가짐
	- ```ob_size``` 변수도 하나 생성되는데 이는 객체가 가진 원소의 수
	- ```ob_digit```의 실제 크기를 나탄냄
	- ```digit```은 설정에 따라 최종적으로 ```unsigned short``` 또는 ```uint32_t```로 변환 = 32비트 부호없는 정수형
##### ob_digit
- 크기가 1로 고정되어 유동적으로 크기를 변활할수 없는것처럼 보인
- 하지만 Python구현체에서는 내부적으로 메모리 관리를 담당하는 부분이 있어, 하나의 ```_longobject```가 실제로 사용할 수 있는 메모리가  ```sizeof(_longobject)```보다 커질 수 있게, ```ob_digit[abs(ob_size)-1]``` 까지를 사용할 수 있도록 만들어줌
#### ob_size
- 일반적으로 객체의 크기
- 정수혀의 부호를 결정하는 역할
- ex) 다섯자리를 사용하는 크기이고 양수라면 ```ob_size``` 는 5가 되고, 음수라면 -5, 0인 경우에는 특별히 이 값을 0으로 두어 객체의 값을 나타냄
#### 값의표현
- 객체의 실제값은 ```ob_digit````배열에 저장
- 0이상 ```abs(ob_size)-1``` 이하의 모든 i에 대해 i번쨰 원소의 값에 2^30i를 곱한 값들을 전부 더하고 ```ob_size```부호를 곱한 것이 실제 값이 된다
![enter image description here](http://www.secmem.org/assets/images/python-biginteger/1.png)
