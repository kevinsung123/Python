from urllib.parse import parse_qs


# import 구문 후 항상 2줄 띄어서 시작하기
def get_first_int(values, key, default=0):
    found = values.get(key, [''])
    if found[0]:
        found = int(found[0])
    else:
        found = default
    return found


my_values = parse_qs('red=5&blue=0&green=', keep_blank_values=True)
print(repr(my_values))
print('Red: ', get_first_int(my_values, 'red'))
print('Green: ', get_first_int(my_values, 'green'))
print('Blue: ', get_first_int(my_values, 'blue'))

