
# 행열
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix)

# 1차원
flat = [x for row in matrix for x in row]
print(flat)

# 제곱하여 새로운 리스트
double_matrix = [[x**2 for x in row] for row in matrix]
print(double_matrix)

# 4보다 큰 짝수값만 가지고 온다
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = [x for x in a if x % 2 == 0]
print(b)
c = [x for x in a if x % 2 == 1]
print(c)

# 행렬에서 행의 합이 10이상이고 3으로 나누어 떨어지는 셀
filtered = [[x for x in row if x % 3 ==0] for row in matrix if sum(row)>=10]
print(filtered)