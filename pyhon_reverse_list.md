### Python List를 reversed 하는방법
#### reversed
```
ans_list = []  
while True:  
    if idx == -1:  
        break  
  ans_list.append(idx)  
    idx = parent[idx]  
ans_list.append(N)
print("원본: ",ans_list)
print("reverse : ",list(reversed(ans_list))
```
####  slicing 사용법
- 일차원 리스트 slicing
``` new_list= ans_list[: :-1]```
- 이차원 리스트 reversed
```
##reverse 복사할떄
arr=[ row[: : -1] for  row in copy] 
##그냥 복사할떄
arr=[ row[: ] for  row in copy] 
```
