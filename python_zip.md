### zip
- 목적 : mulitiple 컨테이너에서 같은 index끼리 map를 사용하기 위한 목적. 마치 single entity 같이 사용
- Syntax : zip(*iterators)
- Parametes : Python iterables or containers(list,string etc)
- Return Value : single iterator object를 리턴

### unzip
- unzipping 은 zippped 된 값들을 원래 상태로 되돌려 놓을때사용  \* operator를 사용 

#### 이차원배열 Transpose
- unzip((zip*)하여 열기준으로 리스트를 뽑아서 다시 list로 만듬 
```
Map = []
for y in range(3):
    tmp = []
    for x in range(3):
        tmp.append((y * 3) + (x + 1))
    Map.append(tmp)
print(Map)
print(Map = list(map(list, zip(*Map))))
print(list(zip(*Map)))
```