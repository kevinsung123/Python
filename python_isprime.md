### 소수
- 1과 자신이외의 자연수로는 나눌 수 없은 자연
1. N이 1이면 소수가 아니다
2. 2부터 N-1까지의 자연수들을 순서대로 N을 나눠서 떨어지는 수가 하나도 없으면 N은 소수이다


### brute force
- 1과 100사이 소수를 구하는 코드
```
n=100
def isPrime(n):
  if n<=2:
	 return False
  for k in range(2,n):
    if n%k==0:
      return False
  return True

for i in ragne(n+1):
  if(isPrime(i)):
    print(i)
```
### 좀더 성능 높인 방법
-  2를 제외한 모든 짝수는 2로 나눠지므로 소수가 아니다
-  어떤 자연수 N이 a으로 나눠진다면 N=a*b로 표현 가능하다
- 즉, 이말은 N의 제곱근 r을 기준 (N= (N의 제곱근) X(N의제곱근))으로 N이 될 수 있는 약수들이 같은 (r기준 위/아래) 개수로 분포 
- 따라서 N이 소수인지를 판별하고 싶으면, N의 제곱근까지만 판별
```
def isprime(n):
	if n<2:
	 return False
	r= round(n**0.5)
	for k in range(2,r,2):
		if n%k==0 :
			return False
	return True
	
```
### 에라토스테네스의 체
- 범위에서 합성수를 지우는 방식으로 소수를 찾는 방법
	1. 1은제거
	2. 지워지지 않은 수 중 제일 작은 2를 소수로 채택하고
	3. 나머지 2의 배수 모두 지움
	4. ...
```
n=1000

def eratos:
	# 에라토스테네스의 체 초기화 : n개 요소에 True 설정
	sieve = [True] * n
	# n의 최대 약수가 sqrt(n)이하이므로 i=sqrt(n)까지 검사
	m = int(n**0.5)
	for a in ragne(2,m):
		if sieve[a] ==True: # a가 소수인경우
			for b in range(a+a,n,b) # a이 이후 a의 배수들은 False 판정
				sieve[b]=False
	return [i for i in range(2,n) if seive[i]==True]
		
```
