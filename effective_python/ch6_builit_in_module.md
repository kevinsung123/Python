### ch6 내장모듈
- python은 표준 라이브러리에 필요한 기능을 갖추는 방법을 취함
- 다른 많은 언어에서는 약간의 공통 패키지를 탑재하고 중요한 기능은 다른곳에서 찾음
- python은 언어를 사용할때 일반적으로 사용하는 기본 모듈은 기본 설치로제공
- 자주쓰는 built-in-module은 언어 사양의 일부이므로 python의 기본 특징과 밀접하게 관련
- 기본 built-in-module은 `복잡한 프로그램을 작성하거나 오류가 일어날 가능성이 큰 프로그램 작성시 특히 중요`
---
#### betterway 42 functools.wraps로 함수 데코레이터를 작성하자
- python에서는 함수에 적용할 수 있는 decorator라는 특별한 문법이 존재
- 함수를 호출하기 전이나 후에 추가로 코드를 실행하는 기능 가짐
- 이 기능으로 아래 2개의 값을 저근하거나 수정 가능
	- `입력 인수`
	- `반환값`
- 이 기능의 목적은
	- `시맨틱강조`
	- `디버깅`
	- `함수등록`
- ex) 함수를 호출할 떄 인수와 반환값을 출력하고싶음 특히 재구호출에서 함수 호출의 스택 디버깅시 유용
```
# functools.wraps로 함수 데코레이터를 정의하자  
from functools import wraps  
  
def trace(func):  
    @wraps(func)  
    def wrapper(*args, **kwargs):  
        result = func(*args, **kwargs)  
        print('%s(%r, %r) -> %r' % (func.__name__, args, kwargs, result))  
        return result  
    return wrapper  
  
  
@trace  
def fibonacci(n):  
    if n in (0, 1):  
        return n  
    return fibonacci(n - 2) + fibonacci(n - 1)  
  
  
fibonacci = trace(fibonacci)  
fibonacci(3)  
help(fibonacci)
**************************output*****************************************'
fibonacci((1,), {}) -> 1
fibonacci((1,), {}) -> 1
fibonacci((0,), {}) -> 0
fibonacci((0,), {}) -> 0
fibonacci((1,), {}) -> 1
fibonacci((1,), {}) -> 1
fibonacci((2,), {}) -> 1
fibonacci((2,), {}) -> 1
fibonacci((3,), {}) -> 2
fibonacci((3,), {}) -> 2
Help on function fibonacci in module __main__

```
- 이 trace decorator 호출시 finbonaaci 실행 전후에 wrapper 코드를 실해앟여 재귀 스택의 각 단계마다 인수와 반환값 출력
- `%s` 지정자는 [`str()`](https://docs.python.org/2/library/functions.html#str) 을 사용하여 객체를 변환하고 `%r`는 [`repr()`](https://docs.python.org/2/library/functions.html#repr)
- decorator는 런타임에 한 함수로 다른 함수를 수정할 수 있게 해주는 파이썬 문법
- decorator를 사용하면 debugger와 같이 객체 내부를 조사하는 도구가 이상하게 동잘할 수 있음
- 직접 decorator를 정의할때 이런문제를 피할려면 `built-in-module functools의 wraps decorator`를 활용하자
---
