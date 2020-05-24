### Python 예외처리 try/except/else/finally에서 각 블록의 장점을 이용
- python 예외처리 과정에서 넣을 수 있는 4번의 구분이 되는 시점
	- try
	- except
	- else
	- finally 
#### finally
- 예외를 전달하고 싶지만, 예외가 발생해도 정리 코드를 실행하고 싶을때 try/finally를 사용
- 일반 ex)  파일 핸들러 제대로 조욜하는 작업
```
handle=open('/tmp/random_data.txt') # IOError 발생 가능성
try :
	data = hadle.read()  # unicodeDecodeError 발생가능성 
finally : 
	handle.close() 	    # try : 이후에 항상 실행됨
```
- read 메서드에서 발생한 예외를 항상 호출 코드까지 전달
- handle의 close메서도 또한 finally블록에서 실행되는 것이 보장
- 파일이 없을때 IOError 
- 파일 열때 일어나느 예외는 finally블록에서 처리하지 않아야하므로 try 블록 앞에서 open 호출

#### else
- 코드에서 어떤 예외를 처리하고 어떤 예외를 전달할지를 명확하게 하려면 try/except/else를 사용
- try 블록이 예외를 일으키지 않으면, else 블록 실행
- else 블록을 사용하면 try블록의 코드를 최소로 줄이고 가독성 높임
- ex) 문자열에서 JSON 딕셔너리 데이터를 로드하여 그안에 든 키 값을 반환
```
def load_json_key(data,key):
	try:
		result_dict=json.loads(data) # Value Error 존재가능성
	except ValueError as e:
		raise KeyError from e
	else :
		return reuslt_dict[key]     # key error 발생가능성
```
- json이 올바르지 않다면, json.loads로 decode할때 ValueError 발생  => except에서 처리 
- decoding 성공시 else 블록에서 키를 찾음
- 키를 찾을때 어떤 예외가 일어나면 그 예외는 try 블록 밖에 있으므로 호출 코드까지 전달
- else 절은 try/except 다음에 나오는 처리를 시각적으로 except블록과 구분
- 예외 전달 행위를 명확하게 전달

#### 모두함계사용
- 복합문 하나로 모든 것을 처리하고 싶다면 try/except/else/finally 를 사용
- 예시 파일에서 수행할 작업 설명을 읽고 처리한 후 즉석에서 파일을 업데이트
	- try 블록을 파일을 일고 처리 
	- except 블록은 try블록에서 일어난 예외를 처리
	- else 블록은 파일을 즉석에서 업데이트하고 이와 관련한 예외가 전달되게 하는데 사용
	- finally  블록은 파일 핸들을 정리하는 사용
