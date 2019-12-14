x, y = input("enter two value : ").split()
print(x)
print(y)


# using type casting list()
x = list(map(int, input().split()))
print("List of num =", x)

# using list comprehension
L = [int(x) for x in input().split()]
print("List comprehension = ", L)


n = int()