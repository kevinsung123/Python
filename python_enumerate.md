# Enumeratre
- enumerate object에서 counter를 추가해주는 built-in 함수
- loop 또는 tuple의 리스트에서 사용가능
enumerate(iterable, start=0)
- Syntax
**Parameters:**
**Iterable:** any object that supports iteration
**Start:** the index value from which the counter is 
              to be started, by default it is 0

```
# Python program to illustrate 
# enumerate function 
l1 = ["eat","sleep","repeat"] 
s1 = "geek"
  
# creating enumerate objects 
obj1 = enumerate(l1) 
obj2 = enumerate(s1) 
  
print "Return type:",type(obj1) 
print list(enumerate(l1)) 
  
# changing start index to 2 from 0 
print list(enumerate(s1,2))
```              
- output
```
Return type: < type 'enumerate' >
[(0, 'eat'), (1, 'sleep'), (2, 'repeat')]
[(2, 'g'), (3, 'e'), (4, 'e'), (5, 'k')]
```
