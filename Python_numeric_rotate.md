### Python 숫자 회전방법
- boj 9019 DSLR문제 참고
- D,S,L,R 연산 중에서 L과 R은 4자리수를 각각 왼쪽 오른쪽으로 한번씩 회전
1. 첫번쨰  =>TLE 시간초과남...
	- 숫자를 문자열로 처리해서 deque의 rotate함수를 쓸생각을함
	```
    
           # 4자리 모두 숫잘일때는 노상관
           # 3,2,1자리일때는 0을채워야함
           if len(str(cur)) == 3:
               cur = '0' + str(cur)
           if len(str(cur)) == 2:
               cur = '00' + str(cur)
           if len(str(cur)) == 1:
               cur = '000' + str(cur)
           tmp = [i for i in str(cur)]
           tmp = deque(tmp)
           tmp.rotate(-1)
           tmp = list(tmp)
           next = ''.join(tmp)
	```
2. 두번쨰 그냥 문자열로 처리하자   => 마찬가지로 시간초과
```
# 4자리 모두 숫잘일때는 노상관  
# 3,2,1자리일때는 0을채워야함  
if len(str(cur)) == 3:  
    cur = '0' + str(cur)  
elif len(str(cur)) == 2:  
    cur = '00' + str(cur)  
elif len(str(cur)) == 1:  
    cur = '000' + str(cur)  
else:  
    cur=str(cur)  
    next = cur[1] + cur[2] + cur[3] + cur[0]
```
3. 숫자 계산
```
def L(n):  # 왼쪽 rotate
    tmp1 = n % 1000 * 10 # 백의 자리수 이하를 구해서 *10  
    tmp2 = int(n / 1000) # 천의 자리수를 일의 자리로 변환   
    print(tmp1 + tmp2)  
    return tmp1 + tmp2  
  
  
def R(n):  # 오른쪽 rotate
    tmp1 = int(n / 10)  # 일의자리를 버림 =>천/백/일의 자리를 구하여=> 백/십/일 자리로변환
    tmp2 = n % 10 * 1000  # 일의 자리를 구하여 *1000
  return tmp1 + tmp2  
  
  
for n in [1234, 990, 9090]:  
    print("n:", n)  
    print("L :",L(n))  
    print("R : ",R(n))
```
