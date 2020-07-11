### Regular Expression in Python
- Regular Expression (RE) 특정패턴(문자열) 찾음
- RE 분석을 위해서 MetaCharaceter들도 잘알고 있어야함
- 다음 14 메타문자들은 기본적으로 익혀야함
```
\   Used to drop the special meaning of character
    following it (discussed below)
[]  Represent a character class
^   Matches the beginning
$   Matches the end
.   Matches any character except newline
?   Matches zero or one occurrence.
|   Means OR (Matches with any of the characters
    separated by it.
*   Any number of occurrences (including 0 occurrences)
+   One or more occurrences
{}  Indicate number of occurrences of a preceding RE 
    to match.
()  Enclose a group of REs
```
---
#### Fucntion compile()
- 정규식 표현들은  pattern object들로 compile
- 이 object들이 다양한 operation들을 지원 searching, matcing ... 
 ```
#Module Regular Expression is imported using __import__(). 
import re 

#compile() creates regular expression character class [a-e], 
#which is equivalent to [abcde]. 
#class [abcde] will match with string with 'a', 'b', 'c', 'd', 'e'. 
p = re.compile('[a-e]') 

#findall() searches for the Regular Expression and return a #list upon finding 
print(p.findall("Aye, said Mr. Gibenson Stark")) 
=>['e', 'a', 'd', 'b', 'e', 'a']
=> case sensitive이므로 소문자 a-e만 찾음
 ```
 - 메타문자 backslash '\' 매우 중요한 역할을 함 
 - 특별한 의미 없이 메타문자를 쓰고 싶으면 '\\'를 활용
 ```
 \d   Matches any decimal digit, this is equivalent
     to the set class [0-9].
\D   Matches any non-digit character.
\s   Matches any whitespace character.
\S   Matches any non-whitespace character
\w   Matches any alphanumeric character, this is
     equivalent to the class [a-zA-Z0-9_].
\W   Matches any non-alphanumeric character.
```
- 예제
```
import re 
# \d is equivalent to [0-9]. 
p = re.compile('\d') 
print(p.findall("I went to him at 11 A.M. on 4th July 1886")) 
  
# \d+ will match a group on [0-9], group of one or greater size 
p = re.compile('\d+') 
print(p.findall("I went to him at 11 A.M. on 4th July 1886")) 

```
--- 
#### Function split()
- character 또는 패턴으로 string을 split 함
- 해당 패턴을 찾으면 그 string에서 나머지 string들을 리턴 
-  syntax
```
re.split(parttern,string,maxsplit=0,flags=0)
- pattern: 문자열을 구분할 pattern
- string : 나눌 문자열
- maxsplit : 나눌 횟수
- flags : ex) flags=re.IGNORECASE => 대소문자 구분안함
```
- 예제
```
from re import split 
  
# '\W+' denotes Non-Alphanumeric Characters or group of characters 
# Upon finding ',' or whitespace ' ', the split(), splits the string from that point 
print(split('\W+', 'Words, words , Words')) 
print(split('\W+', "Word's words Words")) 
  
# Here ':', ' ' ,',' are not AlphaNumeric thus, the point where splitting occurs 
print(split('\W+', 'On 12th Jan 2016, at 11:02 AM')) 
  
# '\d+' denotes Numeric Characters or group of characters 
# Splitting occurs at '12', '2016', '11', '02' only 
print(split('\d+', 'On 12th Jan 2016, at 11:02 AM')) 

```
```
=>output
['Words', 'words', 'Words']
['Word', 's', 'words', 'Words']
['On', '12th', 'Jan', '2016', 'at', '11', '02', 'AM']
['On ', 'th Jan ', ', at ', ':', ' AM']
```
---
#### Function : sub()
- substring 함수
- syntax
```
re.sub(pattern, repl, string, count=0, flags=0)
- pattern : 찾을 패턴
- repl  : 찾은 패턴을 대체할 문자열
- count : 바꿀 횧수
- 
```
- 예시
```
import re 
  
# Regular Expression pattern 'ub' matches the string at "Subject" and "Uber". 
# As the CASE has been ignored, using Flag, 'ub' should match twice with the string 
# Upon matching, 'ub' is replaced by '~*' in "Subject", and in "Uber", 'Ub' is replaced. 
print(re.sub('ub', '~*' , 'Subject has Uber booked already', flags = re.IGNORECASE)) 
  
# Consider the Case Sensitivity, 'Ub' in "Uber", will not be reaplced. 
print(re.sub('ub', '~*' , 'Subject has Uber booked already')) 
  
# As count has been given value 1, the maximum times replacement occurs is 1 
print(re.sub('ub', '~*' , 'Subject has Uber booked already', count=1, flags = re.IGNORECASE)) 
  
# 'r' before the patter denotes RE, \s is for start and end of a String. 
print(re.sub(r'\sAND\s', ' & ', 'Baked Beans And Spam', flags=re.IGNORECASE)) 

```
---
#### Function escape() 
- alphanumerics이 아닌 문자들을 모두 backslash하여 리턴하는 함수
- 임의의 문자열을 정규표현 메타문자들을 포함하고 있으시에 유용
