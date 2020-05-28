### 이차원 리스트 복사
1.  slice 사용하기
```
arr=[ row[:] for  row in copy] 
```
2. list()
```
arr= list(copy)
```
3. copy
```
import copy
arr = copy.copy(tmp)
```
4. deepcopy
```
import copy
arr=copy.deepcopy(tmp)
```
