
def divide(a, b):
    try:
        return a/b
    except ZeroDivisionError as e:
        raise ValueError("Invalid inputs") from e


if __name__ == "__main__":

    print("start")
    res = divide(18, 3)
    print(res)

    zero2 = divide(0, 18)
    # print(res)
    # print(zero)
    print(zero2)
