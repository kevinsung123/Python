

a="abcdef"
print("origin : ",a)
## reverse
print("1.slicing : ",a[::-1])

## LOOP
reverse=[]
index=len(a)
while index>0:
    reverse+=a[index-1]
    index=index-1
print("2. loop : ", ''.join(reverse))

## user join
print("3. join : ",''.join(reversed(a)))