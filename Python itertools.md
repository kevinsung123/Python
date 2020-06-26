# Python itertools function and usage
###
## 순열(permutation)
![ex](./img/perm.PNG)
## 조합(combination)
![ex](./img/comb.PNG)

## product
- 수학에서 2개의 set에대한 Cartesian Product이다
- 모든 순서있는 pairs( all ordered pairs(a,b))에대해 경우의 수를 구함
- 왜사용 ? 주어진 iterator로부터 cartesian product를 구함 (사전순으로 결과가 나옴)
- syntax
    - itertools.product(*iterables,repeat=1)
    - itertools.product(*iterables)
```
Input : arr1 = [1, 2, 3]
arr2 = [5, 6, 7]
Output : [(1, 5), (1, 6), (1, 7), (2, 5), (2, 6), (2, 7), (3, 5), (3, 6), (3, 7)]

Input : arr1 = [10, 12]
arr2 = [8, 9, 10]
Output : [(10, 8), (10, 9), (10, 10), (12, 8), (12, 9), (12, 10)]
```