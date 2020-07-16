### python listcomprehension 조건문
- if/else 조건 있을떄
 ```
[f(x) if condition else g(x) for x in sequence]
```
- if조건만 있을떄
```
[f(x) for x in sequence if condition]
```
- 예시 같은 index에대해서는 0 그 이외의 값은 무한대로 초기화
```
dist = [[ 0 if i == j else int(1e9) for j in range(n)] for i in range(n)]
```
