# Python Type Conversion

## list의 기능

* list.index( value ) : 값을 이용하여 위치를 찾는 기능
* list.extend( [value1, value2] ) : 리스트 뒤에 값을 추가 (‘+’연산자 보다 성능이 좋음)
* list.insert( index, value ) : 원하는 위치에 값을 추가
* list.sort( ) : 값을 순서대로 정렬
* list.reverse( ) : 값을 역순으로 정렬 

## list와 string - split(),join()

* list와 string은 유사
* list = str.split() : string -> list, 공백시 스페이스기준
* " ".join(list) : list->string
* a, b = map(int, sys.stdin.readline().split())
	*  int() : 함수 => type 변환
	*  sys.stdin.readline().split() : 입력받은 한줄의 문자열을 split => 리스트로 변환 
	*  결국 리스트를 map(func,iter) 리스트의 모든 값에대해 int함수 적용시킨 결과
* join()
	* 설명 : The join() method is a string method and returns a string in which the elements of sequence have been joined by str separator
	* string_name.join(iterable) 
	* string_name: It is the name of string in which joined elements of iterable will be stored.
	* string_name은 join시킬시 구분자
	* iterable은  objects capable of returning its members one at a time. Some examples are List, Tuple, String, Dictionary and Set



