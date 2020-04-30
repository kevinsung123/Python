### Creating a Tuple
- tuple은 ()안에 모든 item들을 ,로 구분하여 생성되는 자료구조
- 서로 다른 다양한 타입의 item들을 가질수 있음(integer, float, list, string, etc..)
```
# Different types of tuples

# Empty tuple
my_tuple = ()
print(my_tuple)

# Tuple having integers
my_tuple = (1, 2, 3)
print(my_tuple)

# tuple with mixed datatypes
my_tuple = (1, "Hello", 3.4)
print(my_tuple)

# nested tuple
my_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
print(my_tuple)
### output
()
(1, 2, 3)
(1, 'Hello', 3.4)
('mouse', [8, 4, 6], (1, 2, 3))
```
- ( ) parentheses로 1개의 item만 있으면 불충분하다.  ,(comma)가  필요하며, 그것이 tuple으로 인식 함 
```
my_tuple = ("hello")
print(type(my_tuple))  # <class 'str'>

# Creating a tuple having one element
my_tuple = ("hello",)
print(type(my_tuple))  # <class 'tuple'>

# Parentheses is optional
my_tuple = "hello",
print(type(my_tuple))  # <class 'tuple'>
```
---
### Accessing Tuple Elements
- item에 접근하는 방법은 여러가지 존재
1. indexing
	- operator [ ] 으로  접근 가능 
	- 0번째 인덱스부터 시작 6개 원소라면 = 0...5

### Tuple Methods
- item을 추가하거나/삭제하는것은 불가능
- count ,index
	-  해당 원소의 개수를 구함
	-  index를 리턴

```
my_tuple = ('a', 'p', 'p', 'l', 'e',)
print(my_tuple.count('p'))  # Output: 2
print(my_tuple.index('l'))  # Output: 3
```


