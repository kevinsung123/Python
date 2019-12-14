# 숫자 리스트를 정렬할때 특정 그룹의 숫자들이 먼저 오도록 표현
def sort_priority(values, group):
    def helper(x):
        if x in group:
            return 0, x
        return 1, x
    values.sort(key=helper)


def sort_priority3(number, group):
    found = False

    def helper(x):
        nonlocal found
        if x in group:
            found = True
            return 0, x
        return 1, x
    number.sort(key=helper)
    return found


if __name__ == "__main__":
    numbers = [8, 3, 1, 2, 5, 4, 7, 8]
    groups = {2, 3, 5, 7}
    # sort_priority(numbers, groups)
    print(numbers)
    f = sort_priority3(numbers, groups)
    print("Found : ", f)
    print(numbers)
