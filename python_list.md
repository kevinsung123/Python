### remove 
-  list에서 주어진 object를 지우는 remove() built함수이다 
-  return 값이 없음
- syntax
```
list_name.remove(ojb)

```
- parameter
```
parameter - object to be removed from the list
※Notes:list에서 처음 만난 object를 지운다 
```
- code#1
```
# Python3 program to demonstrate the use of  
# remove() method  
  
  
# the first occurrence of 1 is removed from the list  
list1 = [ 1, 2, 1, 1, 4, 5 ]  
list1.remove(1)  
print(list1)  
  
# removes 'a' from list2  
list2 = [ 'a', 'b', 'c', 'd' ]  
list2.remove('a')  
print(list2) 
```
- output
```
[2, 1, 1, 4, 5]
['b', 'c', 'd']
```
- code 3 : 주어진 리스트에서 모든 1을 제거하는 프로그램
```
# Python3 program for practical application 
# of removing 1 untill all 1 are removed from the list  
   
   
list1 = [1, 2, 3, 4, 1, 1, 1, 4, 5] 
  
# looping till all 1's are removed 
while (list1.count(1)): 
    list1.remove(1)  
      
print(list1)  
```
- output
```
[2, 3, 4, 4, 5]
```
- 예외처리하기 
```
def remove(node):  
    global child  
    try :  
        child[parent[node]].remove(node)  
    except ValueError :  
        pass
```
